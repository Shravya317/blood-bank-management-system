from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from database.db import get_db_connection, close_connection
import datetime

patient_bp = Blueprint('patient', __name__, url_prefix='/patient')

@patient_bp.before_request
def check_patient():
    if session.get('role') != 'patient':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('auth.login'))

@patient_bp.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database Error"
        
    cursor = conn.cursor(dictionary=True)
    
    # 1. Get Patient Profile
    cursor.execute("SELECT * FROM Patient WHERE Patient_ID = %s", (session['user_id'],))
    profile = cursor.fetchone()
    
    # 2. Get all hospitals for the dropdown
    cursor.execute("SELECT * FROM Hospital")
    hospitals = cursor.fetchall()
    
    if hospitals:
        hospitals[0]['is_nearest'] = True
        
    # 3. Get Patient's past requests
    cursor.execute("""
        SELECT R.*, H.Hospital_Name 
        FROM Request R
        JOIN Hospital H ON R.Hospital_ID = H.Hospital_ID
        WHERE R.Patient_ID = %s
        ORDER BY R.Request_Date DESC
    """, (session['user_id'],))
    past_requests = cursor.fetchall()
    
    # Check for fulfilled alerts that haven't been seen yet
    seen_alerts = session.get('seen_alerts_patient', [])
    fulfilled_alerts = [r for r in past_requests if r['Status'] == 'Fulfilled' and r['Request_ID'] not in seen_alerts]
    
    # Mark them as seen for the next time
    if fulfilled_alerts:
        updated_seen = list(seen_alerts) + [r['Request_ID'] for r in fulfilled_alerts]
        session['seen_alerts_patient'] = updated_seen
    
    close_connection(conn, cursor)
    
    return render_template('patient_dashboard.html', 
                           title="Receiver Dashboard", 
                           profile=profile, 
                           hospitals=hospitals,
                           past_requests=past_requests,
                           fulfilled_alerts=fulfilled_alerts)

@patient_bp.route('/request_blood', methods=['POST'])
def request_blood():
    hospital_id = request.form.get('hospital_id')
    blood_group = request.form.get('blood_group')
    qty = request.form.get('qty_required')
    patient_id = session['user_id']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    today = datetime.date.today().strftime('%Y-%m-%d')
    req_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    
    query = """
    INSERT INTO Request (Request_Date, Required_Date, Status, Component_Type, Qty_Required, Priority, Blood_Group, Hospital_ID, Patient_ID)
    VALUES (%s, %s, 'Pending', 'Whole Blood', %s, 'Emergency', %s, %s, %s)
    """
    cursor.execute(query, (today, req_date, qty, blood_group, hospital_id, patient_id))
    conn.commit()
    close_connection(conn, cursor)
    
    flash("Emergency blood request submitted to the selected hospital!", "success")
    return redirect(url_for('patient.dashboard'))

@patient_bp.route('/update_profile', methods=['POST'])
def update_profile():
    name = request.form.get('name')
    blood_group = request.form.get('blood_group')
    gender = request.form.get('gender')
    age = request.form.get('age')
    phone = request.form.get('phone')
    condn = request.form.get('medical_condn')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE Patient SET Name=%s, Blood_Group=%s, Gender=%s, Age=%s, Phone=%s, Medical_Condn=%s WHERE Patient_ID=%s"
    cursor.execute(query, (name, blood_group, gender, age, phone, condn, session['user_id']))
    conn.commit()
    close_connection(conn, cursor)
    
    session['user_name'] = name
    flash("Medical profile updated successfully.", "success")
    return redirect(url_for('patient.dashboard'))
