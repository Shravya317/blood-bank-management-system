from flask import Blueprint, jsonify
import smtplib
from email.mime.text import MIMEText
import random
from config import Config
from flask import render_template, request, redirect, url_for, session, flash
from database.db import get_db_connection, close_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_phone = request.form.get('username')
        password = request.form.get('password')
        role_type = request.form.get('role_type') # 'staff', 'donor', 'hospital', or 'patient'

        conn = get_db_connection()
        if not conn:
            flash("Database connection failed. Is MySQL running?", "danger")
            return redirect(url_for('auth.login'))

        cursor = conn.cursor(dictionary=True)
        user = None

        if role_type == 'staff':
            cursor.execute("SELECT * FROM Staff WHERE Email = %s AND Password = %s", (email_or_phone, password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user['Staff_ID']
                session['user_name'] = user['Name']
                session['role'] = 'staff'
                close_connection(conn, cursor)
                return redirect(url_for('staff.dashboard'))
                
        elif role_type == 'donor':
            cursor.execute("SELECT * FROM Donor WHERE Phone = %s AND Password = %s", (email_or_phone, password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user['Donor_ID']
                session['user_name'] = user['Name']
                session['role'] = 'donor'
                close_connection(conn, cursor)
                return redirect(url_for('donor.dashboard'))

                
        elif role_type == 'hospital':
            cursor.execute("SELECT * FROM Hospital WHERE License_No = %s AND Password = %s", (email_or_phone, password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user['Hospital_ID']
                session['user_name'] = user['Hospital_Name']
                session['role'] = 'hospital'
                close_connection(conn, cursor)
                return redirect(url_for('hospital.dashboard'))
                
        elif role_type == 'patient':
            cursor.execute("SELECT * FROM Patient WHERE Phone = %s AND Password = %s", (email_or_phone, password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user['Patient_ID']
                session['user_name'] = user['Name']
                session['role'] = 'patient'
                close_connection(conn, cursor)
                return redirect(url_for('patient.dashboard'))


        close_connection(conn, cursor)
        elif role == 'ngo':
            cursor.execute('SELECT * FROM NGO WHERE Email = %s', (email,))
            user = cursor.fetchone()
            if user and user['Password'] == password:
                session['user_id'] = user['NGO_ID']
                session['user_name'] = user['Name']
                session['role'] = 'ngo'
                close_connection(conn, cursor)
                return redirect(url_for('ngo.dashboard'))
        flash("Invalid credentials or incorrect role selected.", "danger")
        return redirect(url_for('auth.login'))

    return render_template('login.html', title="Login")



@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        role_type = request.form.get('role_type')
        name = request.form.get('name')
        phone = request.form.get('phone')
        blood_group = request.form.get('blood_group')
        password = request.form.get('password')
        dob = request.form.get('dob') # Add dob
        
        # Calculate age for patient
        age = None
        if dob:
            from datetime import datetime
            try:
                birth_date = datetime.strptime(dob, '%Y-%m-%d')
                today = datetime.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            except ValueError:
                pass

        conn = get_db_connection()
        if not conn:
            flash("Database connection failed.", "danger")
            return redirect(url_for('auth.register'))
        
        cursor = conn.cursor(dictionary=True)
        
        if role_type == 'donor':
            cursor.execute("SELECT * FROM Donor WHERE Phone = %s", (phone,))
            if cursor.fetchone():
                flash("Phone number already registered as Donor.", "danger")
            else:
                cursor.execute("INSERT INTO Donor (Name, Phone, Password, Blood_Group, Date_of_Birth, Status) VALUES (%s, %s, %s, %s, %s, %s)", 
                               (name, phone, password, blood_group, dob, "Active"))
                conn.commit()
                flash("Registration successful! Please login.", "success")
                close_connection(conn, cursor)
                return redirect(url_for('auth.login'))
                
        elif role_type == 'patient':
            cursor.execute("SELECT * FROM Patient WHERE Phone = %s", (phone,))
            if cursor.fetchone():
                flash("Phone number already registered as Receiver.", "danger")
            else:
                cursor.execute("INSERT INTO Patient (Name, Phone, Password, Blood_Group, Age) VALUES (%s, %s, %s, %s, %s)", 
                               (name, phone, password, blood_group, age))
                conn.commit()
                flash("Registration successful! Please login.", "success")
                close_connection(conn, cursor)
                return redirect(url_for('auth.login'))
        else:
            flash("Invalid role selected.", "danger")
            
        close_connection(conn, cursor)
        return redirect(url_for('auth.register'))
        
    return render_template('register.html', title="Register")

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('index'))

@auth_bp.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.json.get('email')
    if not email:
        return jsonify({'success': False, 'message': 'Email required'})
    
    otp = str(random.randint(100000, 999999))
    session['registration_otp'] = otp
    
    try:
        msg = MIMEText(f"Your Blood Bank Registration OTP is: {otp}")
        msg['Subject'] = 'Blood Bank Registration OTP'
        msg['From'] = Config.MAIL_USERNAME
        msg['To'] = email
        
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        server.starttls()
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return jsonify({'success': True, 'message': 'OTP sent'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@auth_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    otp = request.json.get('otp')
    if otp and session.get('registration_otp') == otp:
        return jsonify({'success': True})
    return jsonify({'success': False})

