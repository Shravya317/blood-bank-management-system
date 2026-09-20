from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from database.db import get_db_connection, close_connection
import datetime

donor_bp = Blueprint('donor', __name__, url_prefix='/donor')

@donor_bp.before_request
def check_donor():
    if session.get('role') != 'donor':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('auth.login'))

@donor_bp.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database Error"
        
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Donor WHERE Donor_ID = %s", (session['user_id'],))
    profile = cursor.fetchone()
    
    cursor.execute("SELECT * FROM Donation WHERE Donor_ID = %s ORDER BY Donation_Date DESC", (session['user_id'],))
    donations = cursor.fetchall()
    
    query = """
    SELECT H.Hospital_Name, H.Address, SUM(R.Qty_Required) as Total_Needed, 
           MAX(CASE WHEN R.Priority = 'Emergency' THEN 3 WHEN R.Priority = 'High' THEN 2 ELSE 1 END) as Urgency_Level
    FROM Request R
    JOIN Hospital H ON R.Hospital_ID = H.Hospital_ID
    WHERE R.Blood_Group = %s AND R.Status = 'Pending'
    GROUP BY H.Hospital_ID, H.Hospital_Name, H.Address
    ORDER BY Total_Needed DESC, Urgency_Level DESC
    """
    cursor.execute(query, (profile['Blood_Group'],))
    urgent_needs = cursor.fetchall()

    
    # Fetch active blood camps and check if donor is registered
    cursor.execute("""
        SELECT C.*, 
               (SELECT COUNT(*) FROM Camp_Registration CR WHERE CR.Camp_ID = C.Camp_ID AND CR.Donor_ID = %s) as Is_Registered
        FROM Blood_Camp C
        WHERE C.Camp_Date >= CURRENT_DATE
        ORDER BY C.Camp_Date ASC, C.Start_Time ASC
    """, (session['user_id'],))
    active_camps = cursor.fetchall()
    cursor.execute('SELECT Hospital_ID, Hospital_Name FROM Hospital')
    all_hospitals = cursor.fetchall()
    
    close_connection(conn, cursor)
    
    return render_template('donor_dashboard.html', title="Donor Dashboard", profile=profile, donations=donations, urgent_needs=urgent_needs, all_hospitals=all_hospitals, active_camps=active_camps)

@donor_bp.route('/update_profile', methods=['POST'])
def update_profile():
    name = request.form.get('name')
    blood_group = request.form.get('blood_group')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    dob = request.form.get('dob')
    
    if not dob:
        dob = None
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE Donor SET Name=%s, Blood_Group=%s, Gender=%s, Phone=%s, Date_of_Birth=%s WHERE Donor_ID=%s"
    cursor.execute(query, (name, blood_group, gender, phone, dob, session['user_id']))
    conn.commit()
    close_connection(conn, cursor)
    
    session['user_name'] = name
    flash("Medical profile updated successfully.", "success")
    return redirect(url_for('donor.dashboard'))

@donor_bp.route('/donate', methods=['POST'])
def donate():
    component = request.form.get('component_type')
    last_donated_str = request.form.get('last_donated')
    qty = request.form.get('qty')
    
    if not last_donated_str:
        flash("Please provide your last donated date.", "danger")
        return redirect(url_for('donor.dashboard'))
        
    last_donated = datetime.datetime.strptime(last_donated_str, '%Y-%m-%d').date()
    today = datetime.date.today()
    
    gap_rules = {
        'Whole Blood': 56,
        'Platelets': 7,
        'Plasma': 28,
        'Double Red Cells': 112
    }
    
    required_gap = gap_rules.get(component, 56)
    days_since_last = (today - last_donated).days
    
    if days_since_last < required_gap:
        next_eligible = (last_donated + datetime.timedelta(days=required_gap)).strftime('%Y-%m-%d')
        flash(f"Woah you need to wait right now! The recommended wait time for {component} is {required_gap} days. You can donate again on {next_eligible}.", "danger")
        return redirect(url_for('donor.dashboard'))
        
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        
        destination = request.form.get('destination')
        
        cursor.execute("SELECT Blood_Group FROM Donor WHERE Donor_ID = %s", (session['user_id'],))
        donor = cursor.fetchone()
        
        cursor.execute("""
            INSERT INTO Donation (Donation_Date, Quantity_ML, Donation_Type, Donor_ID)
            VALUES (%s, %s, %s, %s)
        """, (today.strftime('%Y-%m-%d'), qty, component, session['user_id']))
        donation_id = cursor.lastrowid
        
        if destination == 'blood_bank':
            cursor.execute("SELECT Storage_ID FROM Storage LIMIT 1")
            storage = cursor.fetchone()
            storage_id = storage['Storage_ID'] if storage else None
            
            if component == 'Platelets':
                expiry_days = 5
            elif component in ['Whole Blood', 'Double Red Cells']:
                expiry_days = 42
            else:
                expiry_days = 365
            expiry_date = (today + datetime.timedelta(days=expiry_days)).strftime('%Y-%m-%d')
            
            cursor.execute("""
                INSERT INTO Blood_Unit (Donation_ID, Component_Type, Collection_Type, Expiry_Date, Storage_ID, Status, Rh_Factor)
                VALUES (%s, %s, 'Voluntary', %s, %s, 'Available', '+')
            """, (donation_id, component, expiry_date, storage_id))
            flash("Donation recorded successfully and added to Central Blood Bank inventory!", "success")
        else:
            h_id = destination
            bg = donor['Blood_Group']
            # Add to Hospital Inventory directly
            cursor.execute("SELECT * FROM Hospital_Inventory WHERE Hospital_ID = %s AND Blood_Group = %s", (h_id, bg))
            if cursor.fetchone():
                cursor.execute("UPDATE Hospital_Inventory SET Quantity = Quantity + %s WHERE Hospital_ID = %s AND Blood_Group = %s", (1, h_id, bg))
            else:
                cursor.execute("INSERT INTO Hospital_Inventory (Hospital_ID, Blood_Group, Quantity) VALUES (%s, %s, %s)", (h_id, bg, 1))
                
            cursor.execute("SELECT Hospital_Name FROM Hospital WHERE Hospital_ID = %s", (h_id,))
            h_name = cursor.fetchone()['Hospital_Name']
            flash(f"Donation recorded successfully and sent directly to {h_name}!", "success")
        cursor.execute("UPDATE Donor SET Last_Donation_Date = %s WHERE Donor_ID = %s", (today.strftime('%Y-%m-%d'), session['user_id']))
        
        conn.commit()
        flash(f"Donation successful! You donated {qty_ml}ml, which has been processed into {num_units} unit(s) of blood for our inventory.", "success")
        
    except Exception as e:
        flash(f"Error processing donation: {str(e)}", "danger")
        
    finally:
        close_connection(conn, cursor)
        
    return redirect(url_for('donor.dashboard'))


@donor_bp.route('/register_camp', methods=['POST'])
def register_camp():
    camp_id = request.form.get('camp_id')
    donor_id = session['user_id']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Check capacity
    cursor.execute("SELECT Current_Donors, Target_Donors FROM Blood_Camp WHERE Camp_ID = %s", (camp_id,))
    camp = cursor.fetchone()
    
    if not camp:
        flash("Camp not found.", "danger")
        return redirect(url_for('donor.dashboard'))
        
    if camp['Current_Donors'] >= camp['Target_Donors']:
        flash("This blood camp has reached its maximum donor capacity.", "danger")
        return redirect(url_for('donor.dashboard'))
        
    # Register donor
    try:
        cursor.execute("INSERT INTO Camp_Registration (Camp_ID, Donor_ID) VALUES (%s, %s)", (camp_id, donor_id))
        cursor.execute("UPDATE Blood_Camp SET Current_Donors = Current_Donors + 1 WHERE Camp_ID = %s", (camp_id,))
        conn.commit()
        flash("Successfully registered for the blood camp! You can only donate 1 unit.", "success")
    except Exception as e:
        flash("You are already registered for this camp.", "warning")
        
    close_connection(conn, cursor)
    return redirect(url_for('donor.dashboard'))
