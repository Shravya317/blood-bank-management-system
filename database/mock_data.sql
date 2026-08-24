USE bloodbank_db;

-- 1. Insert Staff (Password: admin123)
INSERT INTO Staff (Name, Email, Phone, Role, Password) VALUES 
('Alice Smith', 'alice.smith@bloodbank.com', '555-0101', 'Admin', 'admin123'),
('Dr. Bob Jones', 'bob.jones@bloodbank.com', '555-0102', 'Medical Officer', 'admin123'),
('Charlie Brown', 'charlie.brown@bloodbank.com', '555-0103', 'Technician', 'admin123');

-- 2. Insert Donors (Password: donor123)
INSERT INTO Donor (Name, Gender, Blood_Group, Last_Donation_Date, Date_of_Birth, Status, Phone, Password) VALUES 
('John Doe', 'Male', 'O+', '2026-05-10', '1990-05-15', 'Active', '555-0201', 'donor123'),
('Jane Smith', 'Female', 'A-', '2026-02-20', '1985-08-22', 'Active', '555-0202', 'donor123'),
('Mike Johnson', 'Male', 'B+', '2026-07-01', '1992-11-30', 'Active', '555-0203', 'donor123'),
('Emily Davis', 'Female', 'O-', '2025-12-15', '1995-04-10', 'Active', '555-0204', 'donor123'),
('Sarah Wilson', 'Female', 'AB+', '2026-08-01', '1988-09-05', 'Active', '555-0205', 'donor123');

-- 3. Insert Hospitals (Password: hosp123)
INSERT INTO Hospital (Hospital_Name, Address, License_No, Password) VALUES 
('City General Hospital', '123 Main St, City Center', 'LIC-10001', 'hosp123'),
('Mercy Medical Center', '456 Oak Ave, Northside', 'LIC-10002', 'hosp123'),
('County Regional Hospital', '789 Pine Rd, Southside', 'LIC-10003', 'hosp123');

-- 4. Insert Storage
INSERT INTO Storage (Storage_Type, Location_Name, Temperature) VALUES 
('Refrigerator', 'Main Cold Room - A', 4.0),
('Freezer', 'Deep Freeze - B', -30.0);

-- 5. Insert Donations
INSERT INTO Donation (Donation_Date, Quantity_ML, Hemoglobin_Level, Donation_Type, Donor_ID) VALUES 
('2026-05-10', 450, 14.5, 'Whole Blood', 1),
('2026-02-20', 450, 13.2, 'Whole Blood', 2),
('2026-07-01', 450, 15.1, 'Whole Blood', 3),
('2025-12-15', 450, 13.8, 'Whole Blood', 4),
('2026-08-01', 450, 14.0, 'Whole Blood', 5);

-- 6. Insert Blood Units
INSERT INTO Blood_Unit (Component_Type, Expiry_Date, Collection_Type, Collection_Date, Rh_Factor, Storage_ID, Donation_ID, Staff_ID, Status) VALUES 
('Whole Blood', '2026-09-10', 'Voluntary', '2026-05-10', '+', 1, 1, 3, 'Available'),
('Packed Red Cells', '2026-09-20', 'Voluntary', '2026-02-20', '-', 1, 2, 3, 'Available'),
('Whole Blood', '2026-10-01', 'Voluntary', '2026-07-01', '+', 1, 3, 3, 'Available'),
('Platelets', '2025-12-20', 'Voluntary', '2025-12-15', '-', 1, 4, 3, 'Discarded'), 
('Whole Blood', '2026-11-01', 'Voluntary', '2026-08-01', '+', 1, 5, 3, 'Available');

-- 7. Insert Patient Data (Password: pat123)
INSERT INTO Patient (Name, Age, Gender, Phone, Medical_Condn, Blood_Group, Staff_ID, Password) VALUES 
('Tom Hardy', 45, 'Male', '555-0301', 'Surgery', 'O+', 2, 'pat123'),
('Lucy Liu', 32, 'Female', '555-0302', 'Anemia', 'A-', 2, 'pat123'),
('Bruce Wayne', 35, 'Male', '555-0303', 'Trauma', 'O+', 2, 'pat123');

-- 8. Insert Screening Tests
INSERT INTO Screening_Test (Test_Type, Test_Date, Status, Result, Blood_Unit_ID) VALUES 
('HIV/HBV/HCV/Syphilis', '2026-05-11', 'Completed', 'Negative', 1),
('HIV/HBV/HCV/Syphilis', '2026-02-21', 'Completed', 'Negative', 2),
('HIV/HBV/HCV/Syphilis', '2026-07-02', 'Completed', 'Negative', 3),
('HIV/HBV/HCV/Syphilis', '2025-12-16', 'Completed', 'Positive', 4), 
('HIV/HBV/HCV/Syphilis', '2026-08-02', 'Completed', 'Negative', 5);

-- 9. Insert Requests
-- We need multiple hospitals requesting the same blood type (e.g. O+) to test the Donor Smart Match logic.
INSERT INTO Request (Request_Date, Required_Date, Status, Component_Type, Qty_Required, Priority, Blood_Group, Hospital_ID) VALUES 
('2026-08-20', '2026-08-25', 'Pending', 'Whole Blood', 1, 'High', 'O+', 1), -- Hospital 1 needs 1 unit of O+
('2026-08-22', '2026-08-23', 'Pending', 'Whole Blood', 3, 'Emergency', 'O+', 2), -- Hospital 2 needs 3 units of O+ (highest need)
('2026-08-21', '2026-08-24', 'Pending', 'Packed Red Cells', 2, 'High', 'O+', 3), -- Hospital 3 needs 2 units of O+
('2026-08-15', '2026-08-16', 'Fulfilled', 'Packed Red Cells', 1, 'Emergency', 'A-', 2),
('2026-08-22', '2026-08-26', 'Pending', 'Platelets', 1, 'Routine', 'AB+', 1);

-- 10. Insert Issue
INSERT INTO Issue (Issue_Date, Qty_Issued, Issued_By, Request_ID, Blood_Unit_ID) VALUES 
('2026-08-15', 1, 1, 4, 2);
UPDATE Blood_Unit SET Status = 'Issued' WHERE Blood_Unit_ID = 2;

-- 11. Insert Hospital Inventory
INSERT INTO Hospital_Inventory (Hospital_ID, Blood_Group, Quantity) VALUES 
(1, 'A+', 5),
(1, 'A-', 2),
(1, 'B+', 0),
(1, 'O+', 10),
(1, 'O-', 3),
(1, 'AB+', 2),

(2, 'A+', 3),
(2, 'A-', 0),
(2, 'B+', 7),
(2, 'O+', 15),
(2, 'O-', 2),
(2, 'AB-', 1),

(3, 'A+', 0),
(3, 'B+', 2),
(3, 'O+', 8),
(3, 'O-', 1),
(3, 'AB+', 5);
