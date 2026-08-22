import mysql.connector
from config import Config
import os

def run_sql_file(cursor, filename):
    with open(filename, 'r') as f:
        sql_commands = f.read().split(';')
        for command in sql_commands:
            try:
                if command.strip():
                    cursor.execute(command)
            except Exception as e:
                pass

def init_database():
    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD
        )
        cursor = conn.cursor()
        
        # Drop tables to recreate cleanly
        cursor.execute("USE bloodbank_db")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        tables = ['Issue', 'Request', 'Screening_Test', 'Blood_Unit', 'Storage', 'Donation', 'Hospital', 'Patient', 'Donor', 'Staff']
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        run_sql_file(cursor, os.path.join('database', 'schema.sql'))
        run_sql_file(cursor, os.path.join('database', 'mock_data.sql'))
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database re-initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize database: {e}")

if __name__ == '__main__':
    init_database()
