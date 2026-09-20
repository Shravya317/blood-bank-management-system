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
        WHERE Organizer_Type = 'NGO' AND Organizer_ID = %s
        ORDER BY Camp_Date DESC, Start_Time ASC
    """, (session['user_id'],))
    camps = cursor.fetchall()
    
    close_connection(conn, cursor)
    
    return render_template('ngo_dashboard.html', title="NGO Dashboard", camps=camps)

@ngo_bp.route('/organize_camp', methods=['POST'])
def organize_camp():
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
    INSERT INTO Blood_Camp (Organizer_Type, Organizer_ID, Camp_Date, Start_Time, End_Time, Day_of_Week, Venue, Target_Donors)
    VALUES ('NGO', %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (session['user_id'], camp_date, start_time, end_time, day_of_week, venue, target_donors))
    conn.commit()
    close_connection(conn, cursor)
    
    flash("Blood camp organized successfully! Notifications sent to donors and hospitals.", "success")
    return redirect(url_for('ngo.dashboard'))
