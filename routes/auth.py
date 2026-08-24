from flask import Blueprint, render_template, request, redirect, url_for, session, flash
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
            else:
                cursor.execute("SELECT * FROM Donor WHERE Phone = %s", (email_or_phone,))
                if cursor.fetchone():
                    pass 
                else:
                    cursor.execute("INSERT INTO Donor (Name, Phone, Password, Blood_Group, Status) VALUES (%s, %s, %s, %s, %s)", 
                                   ("New Donor", email_or_phone, password, "O+", "Active"))
                    conn.commit()
                    session['user_id'] = cursor.lastrowid
                    session['user_name'] = "New Donor"
                    session['role'] = 'donor'
                    session['is_new_user'] = True
                    close_connection(conn, cursor)
                    flash("Welcome! Your account has been created. Please update your Medical Profile.", "success")
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
            else:
                cursor.execute("SELECT * FROM Patient WHERE Phone = %s", (email_or_phone,))
                if cursor.fetchone():
                    pass
                else:
                    cursor.execute("INSERT INTO Patient (Name, Phone, Password, Blood_Group) VALUES (%s, %s, %s, %s)", 
                                   ("New Receiver", email_or_phone, password, "O+"))
                    conn.commit()
                    session['user_id'] = cursor.lastrowid
                    session['user_name'] = "New Receiver"
                    session['role'] = 'patient'
                    session['is_new_user'] = True
                    close_connection(conn, cursor)
                    flash("Welcome! Your account has been created. Please update your Medical Profile.", "success")
                    return redirect(url_for('patient.dashboard'))

        close_connection(conn, cursor)
        flash("Invalid credentials or incorrect role selected.", "danger")
        return redirect(url_for('auth.login'))

    return render_template('login.html', title="Login")

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('index'))
