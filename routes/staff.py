from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from database.db import get_db_connection, close_connection
import datetime

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.before_request
def check_staff():
    if session.get('role') != 'staff':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('auth.login'))

@staff_bp.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database Error"
        
    cursor = conn.cursor(dictionary=True)
    
    # 1. Get profile (full ER coverage)
    cursor.execute("SELECT * FROM Staff WHERE Staff_ID = %s", (session['user_id'],))
    profile = cursor.fetchone()

    # 2. Get Advanced Inventory with Expiry & Storage
    query_inv = """
    SELECT B.Blood_Unit_ID, B.Component_Type, B.Expiry_Date, B.Rh_Factor, 
           S.Location_Name, S.Temperature, S.Storage_Type,
           D.Blood_Group
    FROM Blood_Unit B
    JOIN Storage S ON B.Storage_ID = S.Storage_ID
    JOIN Donation Dn ON B.Donation_ID = Dn.Donation_ID
    JOIN Donor D ON Dn.Donor_ID = D.Donor_ID
    WHERE B.Status = 'Available'
    ORDER BY B.Expiry_Date ASC
    """
    cursor.execute(query_inv)
    inventory = cursor.fetchall()
    
    # Compute Condition (Fresh/Expired) and build a summary
    today = datetime.date.today()
    inventory_summary = {}
    for unit in inventory:
        unit['Condition'] = 'Fresh' if unit['Expiry_Date'] >= today else 'Expired'
        bg = unit['Blood_Group']
        if bg not in inventory_summary:
            inventory_summary[bg] = 0
        if unit['Condition'] == 'Fresh':
            inventory_summary[bg] += 1
            
    # 3. Get pending requests (Sorted by Priority)
    query_req = """
    SELECT * FROM Request R 
    JOIN Hospital H ON R.Hospital_ID = H.Hospital_ID 
    WHERE R.Status = 'Pending'
    ORDER BY CASE 
        WHEN R.Priority = 'Emergency' THEN 1 
        WHEN R.Priority = 'High' THEN 2 
        ELSE 3 
    END ASC, R.Request_Date ASC
    """
    cursor.execute(query_req)
    pending_requests = cursor.fetchall()
    
    # 4. Get Issued Logs (tracking where blood went)
    query_issued = """
    SELECT I.Issue_Date, I.Qty_Issued, R.Blood_Group, R.Component_Type, H.Hospital_Name, B.Blood_Unit_ID
    FROM Issue I
    JOIN Request R ON I.Request_ID = R.Request_ID
    JOIN Hospital H ON R.Hospital_ID = H.Hospital_ID
    JOIN Blood_Unit B ON I.Blood_Unit_ID = B.Blood_Unit_ID
    ORDER BY I.Issue_Date DESC
    """
    cursor.execute(query_issued)
    issued_logs = cursor.fetchall()
    
    # 5. Get Screening Tests
    query_tests = """
    SELECT ST.Test_ID, ST.Test_Type, ST.Test_Date, ST.Status, ST.Result, B.Blood_Unit_ID
    FROM Screening_Test ST
    JOIN Blood_Unit B ON ST.Blood_Unit_ID = B.Blood_Unit_ID
    ORDER BY ST.Test_Date DESC
    """
    cursor.execute(query_tests)
    screening_tests = cursor.fetchall()

    close_connection(conn, cursor)
    
    return render_template('staff_dashboard.html', 
                           title="Staff Dashboard", 
                           profile=profile,
                           inventory=inventory, 
                           inventory_summary=inventory_summary,
                           requests=pending_requests,
                           issued_logs=issued_logs,
                           screening_tests=screening_tests)

@staff_bp.route('/fulfill_request', methods=['POST'])
def fulfill_request():
    req_id = request.form.get('request_id')
    bg = request.form.get('blood_group')
    qty = int(request.form.get('qty'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # 1. Find available units matching blood group
    cursor.execute("""
        SELECT B.Blood_Unit_ID 
        FROM Blood_Unit B
        JOIN Donation Dn ON B.Donation_ID = Dn.Donation_ID
        JOIN Donor D ON Dn.Donor_ID = D.Donor_ID
        WHERE B.Status = 'Available' AND D.Blood_Group = %s
        ORDER BY B.Expiry_Date ASC
        LIMIT %s
    """, (bg, qty))
    
    available_units = cursor.fetchall()
    
    if len(available_units) < qty:
        flash(f"Not enough {bg} units available! Needed {qty}, but only {len(available_units)} in stock.", "danger")
    else:
        today = datetime.date.today().strftime('%Y-%m-%d')
        staff_id = session['user_id']
        
        # 2. Issue each unit
        for unit in available_units:
            unit_id = unit['Blood_Unit_ID']
            cursor.execute("UPDATE Blood_Unit SET Status = 'Issued' WHERE Blood_Unit_ID = %s", (unit_id,))
            cursor.execute("""
                INSERT INTO Issue (Issue_Date, Qty_Issued, Issued_By, Request_ID, Blood_Unit_ID)
                VALUES (%s, 1, %s, %s, %s)
            """, (today, staff_id, req_id, unit_id))
            
        # 3. Mark request as fulfilled
        cursor.execute("UPDATE Request SET Status = 'Fulfilled' WHERE Request_ID = %s", (req_id,))
        conn.commit()
        flash(f"Request successfully fulfilled! {qty} units of {bg} issued.", "success")
        
    close_connection(conn, cursor)
    return redirect(url_for('staff.dashboard'))

@staff_bp.route('/discard_unit', methods=['POST'])
def discard_unit():
    unit_id = request.form.get('unit_id')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Blood_Unit SET Status = 'Discarded' WHERE Blood_Unit_ID = %s", (unit_id,))
    conn.commit()
    
    flash(f"Blood Unit #{unit_id} has been safely removed from inventory.", "success")
    close_connection(conn, cursor)
    
    return redirect(url_for('staff.dashboard'))
