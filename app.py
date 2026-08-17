import sqlite3
import os

DB_FILE = "blood_bank.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    
    tables_to_drop = [
        "Donor_Patient_Match", "Issue", "Request", "Screening_Test",
        "Blood_Unit", "Donation", "Patient", "Donor", "Storage", "Staff", "Hospital"
    ]
    for table in tables_to_drop:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")
    
    cursor.execute("""
    CREATE TABLE Hospital (
        Hospital_ID VARCHAR(20) PRIMARY KEY,
        Hospital_Name VARCHAR(100) NOT NULL,
        Address VARCHAR(255),
        License_No VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE Staff (
        Staff_ID VARCHAR(20) PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Role VARCHAR(50) NOT NULL,
        Phone VARCHAR(20),
        Email VARCHAR(100) UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE Storage (
        Storage_ID VARCHAR(20) PRIMARY KEY,
        Storage_Type VARCHAR(50) NOT NULL,
        Location_Name VARCHAR(100) NOT NULL,
        Temperature DECIMAL(4, 2) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE Donor (
        Donor_ID VARCHAR(20) PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Gender CHAR(1) CHECK (Gender IN ('M', 'F', 'O')),
        Blood_Group VARCHAR(5) NOT NULL,
        Date_of_Birth DATE NOT NULL,
        Last_Donation_Date DATE,
        Status VARCHAR(50) DEFAULT 'Eligible',
        Phone VARCHAR(20)
    );
    """)

    cursor.execute("""
    CREATE TABLE Patient (
        Patient_ID VARCHAR(20) PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Age INT NOT NULL CHECK (Age >= 0),
        Gender CHAR(1) CHECK (Gender IN ('M', 'F', 'O')),
        Phone VARCHAR(20),
        Medical_Condn VARCHAR(255),
        Blood_Group VARCHAR(5) NOT NULL,
        Registered_By VARCHAR(20),
        FOREIGN KEY (Registered_By) REFERENCES Staff(Staff_ID)
    );
    """)

    cursor.execute("""
    CREATE TABLE Donation (
        Donation_ID VARCHAR(20) PRIMARY KEY,
        Donor_ID VARCHAR(20) NOT NULL,
        Donation_Date DATE NOT NULL,
        Quantity_ML INT NOT NULL CHECK (Quantity_ML > 0),
        Hemoglobin_Level DECIMAL(4, 2) CHECK (Hemoglobin_Level > 0),
        Donation_Type VARCHAR(50) NOT NULL,
        Collected_By VARCHAR(20),
        FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID),
        FOREIGN KEY (Collected_By) REFERENCES Staff(Staff_ID)
    );
    """)

    cursor.execute("""
    CREATE TABLE Blood_Unit (
        Blood_Unit_ID VARCHAR(20) PRIMARY KEY,
        Donation_ID VARCHAR(20) NOT NULL,
        Component_Type VARCHAR(50) NOT NULL,
        Collection_Date DATE NOT NULL,
        Expiry_Date DATE NOT NULL,
        Rh_Factor CHAR(1) CHECK (Rh_Factor IN ('+', '-')),
        Storage_ID VARCHAR(20),
        Managed_By VARCHAR(20),
        FOREIGN KEY (Donation_ID) REFERENCES Donation(Donation_ID) ON DELETE CASCADE,
        FOREIGN KEY (Storage_ID) REFERENCES Storage(Storage_ID) ON DELETE SET NULL,
        FOREIGN KEY (Managed_By) REFERENCES Staff(Staff_ID) ON DELETE SET NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE Screening_Test (
        Test_ID VARCHAR(20) PRIMARY KEY,
        Blood_Unit_ID VARCHAR(20) NOT NULL UNIQUE,
        Test_Type VARCHAR(50) NOT NULL,
        Test_Date DATE NOT NULL,
        Status VARCHAR(20) CHECK (Status IN ('Pending', 'Completed', 'Cancelled')),
        Result VARCHAR(20) CHECK (Result IN ('Reactive', 'Non-Reactive', 'Indeterminate')),
        FOREIGN KEY (Blood_Unit_ID) REFERENCES Blood_Unit(Blood_Unit_ID) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE Request (
        Request_ID VARCHAR(20) PRIMARY KEY,
        Hospital_ID VARCHAR(20) NOT NULL,
        Request_Date DATE NOT NULL,
        Required_Date DATE NOT NULL,
        Blood_Group VARCHAR(5) NOT NULL,
        Qty_Required INT NOT NULL CHECK (Qty_Required > 0),
        Component_Type VARCHAR(50) NOT NULL,
        Priority VARCHAR(20) CHECK (Priority IN ('Routine', 'Urgent', 'Emergency')),
        Status VARCHAR(20) DEFAULT 'Pending' CHECK (Status IN ('Pending', 'Approved', 'Fulfilled', 'Cancelled')),
        FOREIGN KEY (Hospital_ID) REFERENCES Hospital(Hospital_ID)
    );
    """)

    cursor.execute("""
    CREATE TABLE Issue (
        Issue_ID VARCHAR(20) PRIMARY KEY,
        Request_ID VARCHAR(20) NOT NULL UNIQUE,
        Blood_Unit_ID VARCHAR(20) NOT NULL,
        Issue_Date DATE NOT NULL,
        Qty_Issued INT NOT NULL CHECK (Qty_Issued > 0),
        Issued_By VARCHAR(20) NOT NULL,
        FOREIGN KEY (Request_ID) REFERENCES Request(Request_ID),
        FOREIGN KEY (Blood_Unit_ID) REFERENCES Blood_Unit(Blood_Unit_ID),
        FOREIGN KEY (Issued_By) REFERENCES Staff(Staff_ID)
    );
    """)

    cursor.execute("""
    CREATE TABLE Donor_Patient_Match (
        Donor_ID VARCHAR(20),
        Patient_ID VARCHAR(20),
        Compatibility_Status VARCHAR(50),
        PRIMARY KEY (Donor_ID, Patient_ID),
        FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID) ON DELETE CASCADE,
        FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID) ON DELETE CASCADE
    );
    """)
    
    conn.commit()

def insert_mock_data(conn):
    cursor = conn.cursor()

    hospitals = [
        ("HOSP-01", "City General Hospital", "123 Healthcare Blvd, Sector 4", "LIC-98765-A"),
        ("HOSP-02", "St. Jude Children Hospital", "789 Hope Lane, Medical District", "LIC-43210-B"),
        ("HOSP-03", "Metro Trauma Care Center", "456 Expressway Rd, Junction 2", "LIC-55443-C"),
        ("HOSP-04", "Apex Heart Institute", "88 Cardiac Way, Downtown", "LIC-11223-D"),
        ("HOSP-05", "Sunrise Maternity Clinic", "12 Maternity Drive, Suburb East", "LIC-33445-E")
    ]
    cursor.executemany("INSERT INTO Hospital VALUES (?,?,?,?);", hospitals)

    staff = [
        ("STF-101", "Dr. Alice Vance", "Blood Bank Director", "555-0101", "alice.vance@bloodbank.org"),
        ("STF-102", "Robert Carter", "Lead Lab Technician", "555-0102", "robert.c@bloodbank.org"),
        ("STF-103", "Sarah Jenkins", "Senior Phlebotomist", "555-0103", "sarah.j@bloodbank.org"),
        ("STF-104", "David Miller", "Inventory Administrator", "555-0104", "david.m@bloodbank.org"),
        ("STF-105", "Dr. Marcus Brody", "Quality Officer", "555-0105", "marcus.b@bloodbank.org")
    ]
    cursor.executemany("INSERT INTO Staff VALUES (?,?,?,?,?);", staff)

    storages = [
        ("STR-01", "Blood Refrigerator", "Fridge-A Shelf-1", 4.0),
        ("STR-02", "Platelet Agitator", "Agitator-Cabinet-B", 22.0),
        ("STR-03", "Plasma Ultra-Freezer", "Freezer-C Bay-2", -30.0),
        ("STR-04", "Cryo Storage Vault", "Cryo-Vault-D1", -80.0)
    ]
    cursor.executemany("INSERT INTO Storage VALUES (?,?,?,?);", storages)

    donors = [
        ("DNR-201", "John Doe", "M", "O+", "1988-05-12", "2026-06-15", "Eligible", "555-0201"),
        ("DNR-202", "Jane Smith", "F", "A-", "1993-09-24", "2026-05-10", "Eligible", "555-0202"),
        ("DNR-203", "Michael Johnson", "M", "B+", "1975-11-02", "2026-03-20", "Eligible", "555-0203"),
        ("DNR-204", "Emily Davis", "F", "AB+", "2000-02-14", "2026-07-01", "Eligible", "555-0204"),
        ("DNR-205", "Carlos Santana", "M", "O-", "1985-12-30", "2026-04-18", "Eligible", "555-0205"),
        ("DNR-206", "Priya Sharma", "F", "A+", "1997-08-19", "2026-01-11", "Eligible", "555-0206")
    ]
    cursor.executemany("INSERT INTO Donor VALUES (?,?,?,?,?,?,?,?);", donors)

    patients = [
        ("PAT-301", "Robert Downey", 55, "M", "555-0301", "Severe Anemia", "O+", "STF-101"),
        ("PAT-302", "Angela Bassett", 62, "F", "555-0302", "Leukemia Chemotherapy", "A-", "STF-101"),
        ("PAT-303", "Tom Holland", 28, "M", "555-0303", "Trauma Hemorrhage", "B+", "STF-102"),
        ("PAT-304", "Lisa Kudrow", 42, "F", "555-0304", "Postpartum Hemorrhage", "O-", "STF-103"),
        ("PAT-305", "Vikram Seth", 69, "M", "555-0305", "Coronary Bypass Surgery", "A+", "STF-105")
    ]
    cursor.executemany("INSERT INTO Patient VALUES (?,?,?,?,?,?,?,?);", patients)

    donations = [
        ("DON-401", "DNR-201", "2026-08-01", 450, 14.5, "Whole Blood", "STF-103"),
        ("DON-402", "DNR-202", "2026-08-05", 350, 12.8, "Whole Blood", "STF-103"),
        ("DON-403", "DNR-203", "2026-08-10", 450, 15.2, "Double Red Cells", "STF-103"),
        ("DON-404", "DNR-205", "2026-08-11", 450, 14.0, "Whole Blood", "STF-103"),
        ("DON-405", "DNR-206", "2026-08-12", 450, 13.6, "Apheresis Platelets", "STF-103"),
        ("DON-406", "DNR-204", "2026-08-14", 350, 13.1, "Whole Blood", "STF-103")
    ]
    cursor.executemany("INSERT INTO Donation VALUES (?,?,?,?,?,?,?);", donations)

    blood_units = [
        ("BU-501", "DON-401", "Packed Red Blood Cells", "2026-08-01", "2026-09-12", "+", "STR-01", "STF-102"),
        ("BU-502", "DON-401", "Fresh Frozen Plasma", "2026-08-01", "2027-08-01", "+", "STR-03", "STF-102"),
        ("BU-503", "DON-402", "Packed Red Blood Cells", "2026-08-05", "2026-09-16", "-", "STR-01", "STF-102"),
        ("BU-504", "DON-403", "Platelets", "2026-08-10", "2026-08-15", "+", "STR-02", "STF-102"),
        ("BU-505", "DON-404", "Universal Red Blood Cells", "2026-08-11", "2026-09-22", "-", "STR-01", "STF-102"),
        ("BU-506", "DON-405", "Concentrated Platelets", "2026-08-12", "2026-08-17", "+", "STR-02", "STF-102"),
        ("BU-507", "DON-406", "Cryoprecipitate", "2026-08-14", "2027-08-14", "+", "STR-04", "STF-105")
    ]
    cursor.executemany("INSERT INTO Blood_Unit VALUES (?,?,?,?,?,?,?,?);", blood_units)

    screening_tests = [
        ("TST-601", "BU-501", "Infectious Disease Panel", "2026-08-02", "Completed", "Non-Reactive"),
        ("TST-602", "BU-502", "Infectious Disease Panel", "2026-08-02", "Completed", "Non-Reactive"),
        ("TST-603", "BU-503", "Infectious Disease Panel", "2026-08-06", "Completed", "Non-Reactive"),
        ("TST-604", "BU-504", "Infectious Disease Panel", "2026-08-11", "Completed", "Non-Reactive"),
        ("TST-605", "BU-505", "Emergency Rapid Screening", "2026-08-11", "Completed", "Non-Reactive"),
        ("TST-606", "BU-506", "Infectious Disease Panel", "2026-08-13", "Completed", "Non-Reactive"),
        ("TST-607", "BU-507", "Full Serology Screening", "2026-08-15", "Completed", "Non-Reactive")
    ]
    cursor.executemany("INSERT INTO Screening_Test VALUES (?,?,?,?,?,?);", screening_tests)

    requests = [
        ("REQ-701", "HOSP-01", "2026-08-12", "2026-08-14", "O+", 1, "Packed Red Blood Cells", "Urgent", "Fulfilled"),
        ("REQ-702", "HOSP-02", "2026-08-15", "2026-08-18", "A-", 1, "Packed Red Blood Cells", "Routine", "Fulfilled"),
        ("REQ-703", "HOSP-03", "2026-08-16", "2026-08-16", "B+", 1, "Platelets", "Emergency", "Fulfilled"),
        ("REQ-704", "HOSP-04", "2026-08-16", "2026-08-17", "O-", 1, "Universal Red Blood Cells", "Emergency", "Pending"),
        ("REQ-705", "HOSP-05", "2026-08-17", "2026-08-19", "A+", 1, "Cryoprecipitate", "Routine", "Pending")
    ]
    cursor.executemany("INSERT INTO Request VALUES (?,?,?,?,?,?,?,?,?);", requests)

    issues = [
        ("ISS-801", "REQ-701", "BU-501", "2026-08-13", 1, "STF-104"),
        ("ISS-802", "REQ-702", "BU-503", "2026-08-16", 1, "STF-104"),
        ("ISS-803", "REQ-703", "BU-504", "2026-08-16", 1, "STF-102")
    ]
    cursor.executemany("INSERT INTO Issue VALUES (?,?,?,?,?,?);", issues)

    matches = [
        ("DNR-201", "PAT-301", "Compatible (Exact O+ Match)"),
        ("DNR-202", "PAT-302", "Compatible (Exact A- Match)"),
        ("DNR-205", "PAT-304", "Compatible (Universal Donor O-)"),
        ("DNR-205", "PAT-301", "Compatible (O- to O+ Compatible)"),
        ("DNR-203", "PAT-303", "Compatible (Exact B+ Match)"),
        ("DNR-206", "PAT-305", "Compatible (Exact A+ Match)")
    ]
    cursor.executemany("INSERT INTO Donor_Patient_Match VALUES (?,?,?);", matches)

    conn.commit()

def print_table(title, headers, rows):
    print(f"\n{title}")
    if not rows:
        print("(No data)")
        return
        
    col_widths = [len(h) for h in headers]
    for row in rows:
        for idx, val in enumerate(row):
            val_str = str(val) if val is not None else "NULL"
            col_widths[idx] = max(col_widths[idx], len(val_str))
            
    border = "+" + "+".join(["-" * (w + 2) for w in col_widths]) + "+"
    print(border)
    
    header_str = "|" + "|".join([f" {h:<{col_widths[i]}} " for i, h in enumerate(headers)]) + "|"
    print(header_str)
    print(border)
    
    for row in rows:
        row_str = "|" + "|".join([f" {str(val) if val is not None else 'NULL':<{col_widths[i]}} " for i, val in enumerate(row)]) + "|"
        print(row_str)
    print(border)

def display_tables(conn):
    print("\nDatabase Tables\n")
    
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [row[0] for row in cursor.fetchall()]
    
    for table_name in tables:
        cursor.execute(f"PRAGMA table_info({table_name});")
        headers = [col[1] for col in cursor.fetchall()]
        
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        
        print_table(f"Table: {table_name}", headers, rows)

def display_dashboard(conn):
    print("\n\nOperational Join Reports\n")
    
    cursor = conn.cursor()

    query1 = """
    SELECT 
        D.Name AS Donor,
        D.Blood_Group,
        BU.Blood_Unit_ID,
        BU.Component_Type,
        ST.Result AS Test_Result,
        S.Location_Name AS Storage_Location,
        BU.Expiry_Date
    FROM Donor D
    JOIN Donation Dn ON D.Donor_ID = Dn.Donor_ID
    JOIN Blood_Unit BU ON Dn.Donation_ID = BU.Donation_ID
    JOIN Screening_Test ST ON BU.Blood_Unit_ID = ST.Blood_Unit_ID
    JOIN Storage S ON BU.Storage_ID = S.Storage_ID;
    """
    cursor.execute(query1)
    headers1 = [desc[0] for desc in cursor.description]
    print_table("Inventory Traceability Log", headers1, cursor.fetchall())

    query2 = """
    SELECT 
        H.Hospital_Name,
        R.Request_ID,
        R.Blood_Group,
        R.Component_Type,
        R.Priority,
        R.Status AS Request_Status,
        COALESCE(I.Issue_ID, 'Not Issued') AS Issue_ID,
        COALESCE(I.Issue_Date, 'N/A') AS Issue_Date
    FROM Request R
    JOIN Hospital H ON R.Hospital_ID = H.Hospital_ID
    LEFT JOIN Issue I ON R.Request_ID = I.Request_ID;
    """
    cursor.execute(query2)
    headers2 = [desc[0] for desc in cursor.description]
    print_table("Request Fulfillment Tracker", headers2, cursor.fetchall())

def main():
    print("Blood Bank Management System\n")
    
    conn = get_connection()
    try:
        create_tables(conn)
        insert_mock_data(conn)
        
        display_tables(conn)
        display_dashboard(conn)
        
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
