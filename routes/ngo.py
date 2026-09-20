from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from database.db import get_db_connection, close_connection
import datetime

ngo_bp = Blueprint('ngo', __name__, url_prefix='/ngo')

@ngo_bp.before_request
def check_ngo():
    if session.get('role') != 'ngo':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('auth.login'))

@ngo_bp.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database Error"
        
    cursor = conn.cursor(dictionary=True)
    
    # Fetch camps organized by this NGO
    cursor.execute("""
        SELECT * FROM Blood_Camp 
        WHERE Organizer_Type = 'NGO' AND Organizer_ID = %s AND Status = 'Upcoming'
        ORDER BY Camp_Date DESC, Start_Time ASC
    """, (session['user_id'],))
    camps = cursor.fetchall()
    
    close_connection(conn, cursor)
    
    
    cursor.execute("SELECT * FROM System_Notification ORDER BY Created_At DESC LIMIT 10")
    system_notifications = cursor.fetchall()
    return render_template('ngo_dashboard.html', title="NGO Dashboard", camps=camps, system_notifications=system_notifications)

@ngo_bp.route('/organize_camp', methods=['POST'])
def organize_camp():
    camp_name = request.form.get('camp_name')
    camp_date = request.form.get('camp_date')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    venue = request.form.get('venue')
    target_donors = request.form.get('target_donors')
    
    # Calculate Day of week
    date_obj = datetime.datetime.strptime(camp_date, '%Y-%m-%d')
    day_of_week = date_obj.strftime('%A')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO Blood_Camp (Camp_Name, Organizer_Type, Organizer_ID, Camp_Date, Start_Time, End_Time, Day_of_Week, Venue, Target_Donors)
    VALUES (%s, 'NGO', %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (camp_name, session['user_id'], camp_date, start_time, end_time, day_of_week, venue, target_donors))
    conn.commit()
    close_connection(conn, cursor)
    
    flash("Blood camp organized successfully! Notifications sent to donors and hospitals.", "success")
    return redirect(url_for('ngo.dashboard'))


@ngo_bp.route('/complete_camp/<int:camp_id>', methods=['POST'])
def complete_camp(camp_id):
    if 'user_id' not in session or session.get('role') != 'ngo':
        return redirect(url_for('auth.login'))
        
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Blood_Camp WHERE Camp_ID = %s AND Organizer_Type = 'NGO' AND Organizer_ID = %s", (camp_id, session['user_id']))
    camp = cursor.fetchone()
    if not camp or camp['Status'] == 'Completed':
        flash("Invalid camp.", "danger")
        return redirect(url_for('ngo.dashboard'))
        
    cursor.execute("UPDATE Blood_Camp SET Status = 'Completed' WHERE Camp_ID = %s", (camp_id,))
    
    cursor.execute("""
        SELECT D.Donor_ID, D.Blood_Group
        FROM Camp_Registration CR
        JOIN Donor D ON CR.Donor_ID = D.Donor_ID
        WHERE CR.Camp_ID = %s
    """, (camp_id,))
    donors = cursor.fetchall()
    
    blood_group_counts = {}
    for d in donors:
        cursor.execute("INSERT INTO Donation (Donor_ID, Donation_Date, Status) VALUES (%s, %s, 'Completed')", (d['Donor_ID'], camp['Camp_Date']))
        donation_id = cursor.lastrowid
        cursor.execute("INSERT INTO Blood_Unit (Donation_ID, Component_Type, Expiry_Date, Status) VALUES (%s, 'Whole Blood', DATE_ADD(%s, INTERVAL 42 DAY), 'Available')", (donation_id, camp['Camp_Date']))
        bg = d['Blood_Group']
        blood_group_counts[bg] = blood_group_counts.get(bg, 0) + 1
        
    total_units = len(donors)
    msg_parts = [f"{count} unit(s) of {bg}" for bg, count in blood_group_counts.items()]
    breakdown = ", ".join(msg_parts) if msg_parts else "No blood collected."
    
    message = f"Blood camp '{camp['Camp_Name']}' organized by NGO has successfully concluded! A total of {total_units} unit(s) were collected and added to the central blood bank. Breakdown: {breakdown}."
    
    cursor.execute("INSERT INTO System_Notification (Title, Message) VALUES (%s, %s)", (f"Camp Completed: {camp['Camp_Name']}", message))
    conn.commit()
    close_connection(conn, cursor)
    
    flash("Camp marked as completed and blood units added to inventory!", "success")
    return redirect(url_for('ngo.dashboard'))
