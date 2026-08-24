CREATE DATABASE IF NOT EXISTS bloodbank_db;
USE bloodbank_db;

-- 1. Staff Table
CREATE TABLE Staff (
    Staff_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Role VARCHAR(50),
    Password VARCHAR(255) NOT NULL -- Required for Staff login
);

-- 2. Donor Table
CREATE TABLE Donor (
    Donor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    Blood_Group VARCHAR(5) NOT NULL,
    Last_Donation_Date DATE,
    Date_of_Birth DATE,
    Status VARCHAR(20) DEFAULT 'Active',
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL -- Required for Donor login
);

-- 3. Patient Table
CREATE TABLE Patient (
    Patient_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(20),
    Medical_Condn VARCHAR(255),
    Blood_Group VARCHAR(5) NOT NULL,
    Staff_ID INT, -- collected_by relationship
    Password VARCHAR(255) NOT NULL, -- Required for Patient login
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

-- 4. Hospital Table
CREATE TABLE Hospital (
    Hospital_ID INT AUTO_INCREMENT PRIMARY KEY,
    Hospital_Name VARCHAR(150) NOT NULL,
    Address VARCHAR(255),
    License_No VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL -- Required for Hospital login
);

-- 5. Donation Table
CREATE TABLE Donation (
    Donation_ID INT AUTO_INCREMENT PRIMARY KEY,
    Donation_Date DATE NOT NULL,
    Quantity_ML INT,
    Hemoglobin_Level DECIMAL(5,2),
    Donation_Type VARCHAR(50),
    Donor_ID INT NOT NULL,
    FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID)
);

-- 6. Storage Table
CREATE TABLE Storage (
    Storage_ID INT AUTO_INCREMENT PRIMARY KEY,
    Storage_Type VARCHAR(50),
    Location_Name VARCHAR(100),
    Temperature DECIMAL(5,2)
);

-- 7. Blood_Unit Table
CREATE TABLE Blood_Unit (
    Blood_Unit_ID INT AUTO_INCREMENT PRIMARY KEY,
    Component_Type VARCHAR(50),
    Expiry_Date DATE,
    Collection_Type VARCHAR(50),
    Collection_Date DATE,
    Rh_Factor VARCHAR(5),
    Storage_ID INT,
    Donation_ID INT,
    Staff_ID INT, -- managed relationship
    Status VARCHAR(50) DEFAULT 'Available', -- e.g., Available, Issued, Discarded
    FOREIGN KEY (Storage_ID) REFERENCES Storage(Storage_ID),
    FOREIGN KEY (Donation_ID) REFERENCES Donation(Donation_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

-- 8. Screening_Test Table
CREATE TABLE Screening_Test (
    Test_ID INT AUTO_INCREMENT PRIMARY KEY,
    Test_Type VARCHAR(100),
    Test_Date DATE,
    Status VARCHAR(50),
    Result VARCHAR(50),
    Blood_Unit_ID INT,
    FOREIGN KEY (Blood_Unit_ID) REFERENCES Blood_Unit(Blood_Unit_ID)
);

-- 9. Request Table
CREATE TABLE Request (
    Request_ID INT AUTO_INCREMENT PRIMARY KEY,
    Request_Date DATE NOT NULL,
    Required_Date DATE,
    Status VARCHAR(50) DEFAULT 'Pending',
    Component_Type VARCHAR(50),
    Qty_Required INT NOT NULL,
    Priority VARCHAR(20),
    Blood_Group VARCHAR(5) NOT NULL,
    Hospital_ID INT NOT NULL,
    Patient_ID INT,
    FOREIGN KEY (Hospital_ID) REFERENCES Hospital(Hospital_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

-- 10. Issue Table
CREATE TABLE Issue (
    Issue_ID INT AUTO_INCREMENT PRIMARY KEY,
    Issue_Date DATE NOT NULL,
    Qty_Issued INT,
    Issued_By INT, -- Staff_ID
    Request_ID INT,
    Blood_Unit_ID INT,
    FOREIGN KEY (Issued_By) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Request_ID) REFERENCES Request(Request_ID),
    FOREIGN KEY (Blood_Unit_ID) REFERENCES Blood_Unit(Blood_Unit_ID)
);

-- 11. Hospital_Inventory Table
CREATE TABLE Hospital_Inventory (
    Inventory_ID INT AUTO_INCREMENT PRIMARY KEY,
    Hospital_ID INT NOT NULL,
    Blood_Group VARCHAR(5) NOT NULL,
    Quantity INT DEFAULT 0,
    Last_Updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (Hospital_ID) REFERENCES Hospital(Hospital_ID)
);
