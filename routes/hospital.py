from flask import Blueprint, render_template, session, redirect, url_for, request, flash, jsonify
from database.db import get_db_connection, close_connection
import datetime

hospital_bp = Blueprint('hospital', __name__, url_prefix='/hospital')

@hospital_bp.before_request
def check_hospital():
    if session.get('role') != 'hospital':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('auth.login'))

@hospital_bp.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database Error"
        
    cursor = conn.cursor(dictionary=True)
    
    # Get all hospitals for the switching dropdown
    cursor.execute("SELECT Hospital_ID, Hospital_Name FROM Hospital")
    all_hospitals = cursor.fetchall()
    
    # Get past requests made by this hospital, Approved (Fulfilled) on top
    query = """
    SELECT * FROM Request 
    WHERE Hospital_ID = %s AND Patient_ID IS NULL
    ORDER BY CASE WHEN Status = 'Fulfilled' THEN 1 ELSE 2 END ASC, Request_Date DESC
    """
    cursor.execute(query, (session['user_id'],))
    requests = cursor.fetchall()
    
    # Check for fulfilled alerts that haven't been seen yet
    seen_alerts = session.get('seen_alerts', [])
    new_fulfilled_alerts = [r for r in requests if r['Status'] == 'Fulfilled' and r['Request_ID'] not in seen_alerts]
    
    # Mark them as seen for the next time
    if new_fulfilled_alerts:
        updated_seen = list(seen_alerts) + [r['Request_ID'] for r in new_fulfilled_alerts]
        session['seen_alerts'] = updated_seen
    
        # Fetch Hospital Inventory
    cursor.execute("SELECT * FROM Hospital_Inventory WHERE Hospital_ID = %s", (session['user_id'],))
    inventory = cursor.fetchall()
    inv_dict = {item['Blood_Group']: item['Quantity'] for item in inventory}

    # Get incoming Patient Requests
    cursor.execute("""
        SELECT R.*, P.Name as Patient_Name, P.Phone 
        FROM Request R
        JOIN Patient P ON R.Patient_ID = P.Patient_ID
        WHERE R.Hospital_ID = %s AND R.Patient_ID IS NOT NULL
        ORDER BY CASE WHEN R.Status = 'Pending' THEN 1 ELSE 2 END ASC, R.Request_Date DESC
    """, (session['user_id'],))
    patient_requests = cursor.fetchall()
    
    close_connection(conn, cursor)
    
    return render_template('hospital_dashboard.html', 
                           title="Hospital Dashboard", 
                           requests=requests, 
                           all_hospitals=all_hospitals,
                           new_fulfilled_alerts=new_fulfilled_alerts,
                           inventory=inv_dict,
                           patient_requests=patient_requests)

@hospital_bp.route('/switch_hospital', methods=['POST'])
def switch_hospital():
    new_hospital_id = request.form.get('hospital_id')
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Hospital_Name FROM Hospital WHERE Hospital_ID = %s", (new_hospital_id,))
    hosp = cursor.fetchone()
    close_connection(conn, cursor)
    
    if hosp:
        session['user_id'] = new_hospital_id
        session['user_name'] = hosp['Hospital_Name']
        flash(f"Successfully switched to {hosp['Hospital_Name']}", "success")
        
    return redirect(url_for('hospital.dashboard'))

# API endpoint for the instant match preview
@hospital_bp.route('/api/check_match')
def check_match():
    bg = request.args.get('blood_group')
    if not bg:
        return jsonify({"count": 0})
        
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Simple match: check how many available units exist for this exact blood group
    # Note: In real life, O- is universal, etc. For this DBMS project, we'll just do an exact match query for speed.
    query = """
    SELECT COUNT(*) as available_units 
    FROM Donor D 
    JOIN Donation Dn ON D.Donor_ID = Dn.Donor_ID 
    JOIN Blood_Unit B ON Dn.Donation_ID = B.Donation_ID 
    WHERE B.Status = 'Available' AND D.Blood_Group = %s
    """
    cursor.execute(query, (bg,))
    result = cursor.fetchone()
    
    close_connection(conn, cursor)
    
    return jsonify({"count": result['available_units'] if result else 0})

@hospital_bp.route('/request_blood', methods=['POST'])
def request_blood():
    blood_group = request.form.get('blood_group')
    component = request.form.get('component_type')
    qty = request.form.get('qty_required')
    priority = request.form.get('priority')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    today = datetime.date.today().strftime('%Y-%m-%d')
    req_date = (datetime.date.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d') # default 2 days out
    
    query = """
    INSERT INTO Request (Request_Date, Required_Date, Status, Component_Type, Qty_Required, Priority, Blood_Group, Hospital_ID)
    VALUES (%s, %s, 'Pending', %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (today, req_date, component, qty, priority, blood_group, session['user_id']))
    conn.commit()
    close_connection(conn, cursor)
    
    flash("Blood request submitted successfully!", "success")
    return redirect(url_for('hospital.dashboard'))

@hospital_bp.route('/fulfill_patient_request', methods=['POST'])
def fulfill_patient_request():
    req_id = request.form.get('request_id')
    bg = request.form.get('blood_group')
    qty = int(request.form.get('qty'))
    h_id = session['user_id']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT Quantity FROM Hospital_Inventory WHERE Hospital_ID = %s AND Blood_Group = %s", (h_id, bg))
    inv = cursor.fetchone()
    
    if inv and inv['Quantity'] >= qty:
        cursor.execute("UPDATE Hospital_Inventory SET Quantity = Quantity - %s WHERE Hospital_ID = %s AND Blood_Group = %s", (qty, h_id, bg))
        cursor.execute("UPDATE Request SET Status = 'Fulfilled' WHERE Request_ID = %s", (req_id,))
        conn.commit()
        flash(f"Patient request fulfilled! {qty} units of {bg} deducted from your internal stock.", "success")
    else:
        flash(f"Insufficient internal stock! You need {qty} units of {bg}, please request more from the central blood bank first.", "danger")
        
    close_connection(conn, cursor)
    return redirect(url_for('hospital.dashboard'))
