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
    
    close_connection(conn, cursor)
    
    return render_template('donor_dashboard.html', title="Donor Dashboard", profile=profile, donations=donations, urgent_needs=urgent_needs)

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
        cursor.execute("SELECT Blood_Group FROM Donor WHERE Donor_ID = %s", (session['user_id'],))
        donor = cursor.fetchone()
        
        cursor.execute("""
            INSERT INTO Donation (Donation_Date, Quantity_ML, Donation_Type, Donor_ID)
            VALUES (%s, %s, %s, %s)
        """, (today.strftime('%Y-%m-%d'), qty, component, session['user_id']))
        donation_id = cursor.lastrowid
        
        cursor.execute("SELECT Storage_ID FROM Storage LIMIT 1")
        storage = cursor.fetchone()
        storage_id = storage['Storage_ID'] if storage else None
        
        expiry_days = 35 if component == 'Whole Blood' else (5 if component == 'Platelets' else 365)
        expiry_date = (today + datetime.timedelta(days=expiry_days)).strftime('%Y-%m-%d')
        
        qty_ml = int(qty)
        num_units = max(1, round(qty_ml / 450))
        
        for _ in range(num_units):
            cursor.execute("""
                INSERT INTO Blood_Unit (Component_Type, Expiry_Date, Collection_Date, Rh_Factor, Storage_ID, Donation_ID, Status)
                VALUES (%s, %s, %s, '+', %s, %s, 'Available')
            """, (component, expiry_date, today.strftime('%Y-%m-%d'), storage_id, donation_id))
        
        cursor.execute("UPDATE Donor SET Last_Donation_Date = %s WHERE Donor_ID = %s", (today.strftime('%Y-%m-%d'), session['user_id']))
        
        conn.commit()
        flash(f"Donation successful! You donated {qty_ml}ml, which has been processed into {num_units} unit(s) of blood for our inventory.", "success")
        
    except Exception as e:
        flash(f"Error processing donation: {str(e)}", "danger")
        
    finally:
        close_connection(conn, cursor)
        
    return redirect(url_for('donor.dashboard'))
