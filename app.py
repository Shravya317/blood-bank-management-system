from flask import Flask, render_template, redirect, url_for, session
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from routes.auth import auth_bp
    from routes.staff import staff_bp
    from routes.donor import donor_bp
    from routes.hospital import hospital_bp
    from routes.patient import patient_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(staff_bp, url_prefix='/staff')
    app.register_blueprint(donor_bp, url_prefix='/donor')
    app.register_blueprint(hospital_bp, url_prefix='/hospital')
    app.register_blueprint(patient_bp, url_prefix='/patient')

    @app.route('/')
    def index():
        if 'role' in session:
            if session['role'] == 'staff':
                return redirect(url_for('staff.dashboard'))
            elif session['role'] == 'donor':
                return redirect(url_for('donor.dashboard'))
            elif session['role'] == 'hospital':
                return redirect(url_for('hospital.dashboard'))
            elif session['role'] == 'patient':
                return redirect(url_for('patient.dashboard'))
        return redirect(url_for('auth.login'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
