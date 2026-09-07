-- Database Dump for Friend's Laptop

-- Data for Hospital
INSERT INTO `Hospital` (`Hospital_ID`, `Hospital_Name`, `Address`, `License_No`, `Password`) VALUES (1, 'City General Hospital', '123 Main St, City Center', 'LIC-10001', 'hosp123');
INSERT INTO `Hospital` (`Hospital_ID`, `Hospital_Name`, `Address`, `License_No`, `Password`) VALUES (2, 'Mercy Medical Center', '456 Oak Ave, Northside', 'LIC-10002', 'hosp123');
INSERT INTO `Hospital` (`Hospital_ID`, `Hospital_Name`, `Address`, `License_No`, `Password`) VALUES (3, 'County Regional Hospital', '789 Pine Rd, Southside', 'LIC-10003', 'hosp123');

-- Data for Staff
INSERT INTO `Staff` (`Staff_ID`, `Name`, `Email`, `Phone`, `Role`, `Password`) VALUES (1, 'Alice Smith', 'alice.smith@bloodbank.com', '555-0101', 'Admin', 'admin123');
INSERT INTO `Staff` (`Staff_ID`, `Name`, `Email`, `Phone`, `Role`, `Password`) VALUES (2, 'Dr. Bob Jones', 'bob.jones@bloodbank.com', '555-0102', 'Medical Officer', 'admin123');
INSERT INTO `Staff` (`Staff_ID`, `Name`, `Email`, `Phone`, `Role`, `Password`) VALUES (3, 'Charlie Brown', 'charlie.brown@bloodbank.com', '555-0103', 'Technician', 'admin123');

-- Data for Donor
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (1, 'John Doe', 'Male', 'O+', '2026-09-07', '1990-05-15', 'Active', '555-0201', 'donor123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (2, 'Jane Smith', 'Female', 'A-', '2026-02-20', '1985-08-22', 'Active', '555-0202', 'donor123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (3, 'Mike Johnson', 'Male', 'B+', '2026-07-01', '1992-11-30', 'Active', '555-0203', 'donor123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (4, 'Emily Davis', 'Female', 'O-', '2025-12-15', '1995-04-10', 'Active', '555-0204', 'donor123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (5, 'Sarah Wilson', 'Female', 'AB+', '2026-08-01', '1988-09-05', 'Active', '555-0205', 'donor123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (6, 'External Source', NULL, 'O+', NULL, NULL, 'Active', 'EXT-O+', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (7, 'External Source', NULL, 'O-', NULL, NULL, 'Active', 'EXT-O-', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (8, 'External Source', NULL, 'A+', NULL, NULL, 'Active', 'EXT-A+', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (9, 'External Source', NULL, 'A-', NULL, NULL, 'Active', 'EXT-A-', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (10, 'External Source', NULL, 'B+', NULL, NULL, 'Active', 'EXT-B+', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (11, 'External Source', NULL, 'B-', NULL, NULL, 'Active', 'EXT-B-', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (12, 'External Source', NULL, 'AB+', NULL, NULL, 'Active', 'EXT-AB+', 'ext123');
INSERT INTO `Donor` (`Donor_ID`, `Name`, `Gender`, `Blood_Group`, `Last_Donation_Date`, `Date_of_Birth`, `Status`, `Phone`, `Password`) VALUES (13, 'External Source', NULL, 'AB-', NULL, NULL, 'Active', 'EXT-AB-', 'ext123');

-- Data for Patient
INSERT INTO `Patient` (`Patient_ID`, `Name`, `Age`, `Gender`, `Phone`, `Medical_Condn`, `Blood_Group`, `Staff_ID`, `Password`) VALUES (1, 'Shravya', 45, 'Male', '555-0301', 'Surgery', 'O+', 2, 'pat123');
INSERT INTO `Patient` (`Patient_ID`, `Name`, `Age`, `Gender`, `Phone`, `Medical_Condn`, `Blood_Group`, `Staff_ID`, `Password`) VALUES (2, 'Lucy Liu', 32, 'Female', '555-0302', 'Anemia', 'A-', 2, 'pat123');
INSERT INTO `Patient` (`Patient_ID`, `Name`, `Age`, `Gender`, `Phone`, `Medical_Condn`, `Blood_Group`, `Staff_ID`, `Password`) VALUES (3, 'Bruce Wayne', 35, 'Male', '555-0303', 'Trauma', 'O+', 2, 'pat123');

-- Data for Donation
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (1, '2026-05-10', 450, '14.50', 'Whole Blood', 1);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (2, '2026-02-20', 450, '13.20', 'Whole Blood', 2);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (3, '2026-07-01', 450, '15.10', 'Whole Blood', 3);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (4, '2025-12-15', 450, '13.80', 'Whole Blood', 4);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (5, '2026-08-01', 450, '14.00', 'Whole Blood', 5);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (6, '2026-09-07', 900, NULL, 'Whole Blood', 1);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (7, '2026-09-07', NULL, NULL, 'External Transfer', 6);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (8, '2026-09-07', NULL, NULL, 'External Transfer', 6);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (9, '2026-09-07', NULL, NULL, 'External Transfer', 6);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (10, '2026-09-07', NULL, NULL, 'External Transfer', 6);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (11, '2026-09-07', NULL, NULL, 'External Transfer', 6);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (12, '2026-09-07', NULL, NULL, 'External Transfer', 6);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (13, '2026-09-07', NULL, NULL, 'External Transfer', 7);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (14, '2026-09-07', NULL, NULL, 'External Transfer', 7);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (15, '2026-09-07', NULL, NULL, 'External Transfer', 7);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (16, '2026-09-07', NULL, NULL, 'External Transfer', 7);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (17, '2026-09-07', NULL, NULL, 'External Transfer', 7);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (18, '2026-09-07', NULL, NULL, 'External Transfer', 7);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (19, '2026-09-07', NULL, NULL, 'External Transfer', 8);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (20, '2026-09-07', NULL, NULL, 'External Transfer', 8);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (21, '2026-09-07', NULL, NULL, 'External Transfer', 8);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (22, '2026-09-07', NULL, NULL, 'External Transfer', 8);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (23, '2026-09-07', NULL, NULL, 'External Transfer', 8);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (24, '2026-09-07', NULL, NULL, 'External Transfer', 8);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (25, '2026-09-07', NULL, NULL, 'External Transfer', 9);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (26, '2026-09-07', NULL, NULL, 'External Transfer', 9);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (27, '2026-09-07', NULL, NULL, 'External Transfer', 9);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (28, '2026-09-07', NULL, NULL, 'External Transfer', 9);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (29, '2026-09-07', NULL, NULL, 'External Transfer', 9);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (30, '2026-09-07', NULL, NULL, 'External Transfer', 9);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (31, '2026-09-07', NULL, NULL, 'External Transfer', 10);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (32, '2026-09-07', NULL, NULL, 'External Transfer', 10);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (33, '2026-09-07', NULL, NULL, 'External Transfer', 10);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (34, '2026-09-07', NULL, NULL, 'External Transfer', 10);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (35, '2026-09-07', NULL, NULL, 'External Transfer', 10);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (36, '2026-09-07', NULL, NULL, 'External Transfer', 10);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (37, '2026-09-07', NULL, NULL, 'External Transfer', 11);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (38, '2026-09-07', NULL, NULL, 'External Transfer', 11);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (39, '2026-09-07', NULL, NULL, 'External Transfer', 11);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (40, '2026-09-07', NULL, NULL, 'External Transfer', 11);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (41, '2026-09-07', NULL, NULL, 'External Transfer', 11);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (42, '2026-09-07', NULL, NULL, 'External Transfer', 11);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (43, '2026-09-07', NULL, NULL, 'External Transfer', 12);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (44, '2026-09-07', NULL, NULL, 'External Transfer', 12);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (45, '2026-09-07', NULL, NULL, 'External Transfer', 12);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (46, '2026-09-07', NULL, NULL, 'External Transfer', 12);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (47, '2026-09-07', NULL, NULL, 'External Transfer', 12);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (48, '2026-09-07', NULL, NULL, 'External Transfer', 12);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (49, '2026-09-07', NULL, NULL, 'External Transfer', 13);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (50, '2026-09-07', NULL, NULL, 'External Transfer', 13);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (51, '2026-09-07', NULL, NULL, 'External Transfer', 13);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (52, '2026-09-07', NULL, NULL, 'External Transfer', 13);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (53, '2026-09-07', NULL, NULL, 'External Transfer', 13);
INSERT INTO `Donation` (`Donation_ID`, `Donation_Date`, `Quantity_ML`, `Hemoglobin_Level`, `Donation_Type`, `Donor_ID`) VALUES (54, '2026-09-07', NULL, NULL, 'External Transfer', 13);

-- Data for Storage
INSERT INTO `Storage` (`Storage_ID`, `Storage_Type`, `Location_Name`, `Temperature`) VALUES (1, 'Refrigerator', 'Main Cold Room - A', '4.00');
INSERT INTO `Storage` (`Storage_ID`, `Storage_Type`, `Location_Name`, `Temperature`) VALUES (2, 'Freezer', 'Deep Freeze - B', '-30.00');

-- Data for Blood_Unit
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (1, 'Whole Blood', '2026-09-10', 'Voluntary', '2026-05-10', '+', 1, 1, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (2, 'Packed Red Cells', '2026-09-20', 'Voluntary', '2026-02-20', '-', 1, 2, 3, 'Issued');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (3, 'Whole Blood', '2026-10-01', 'Voluntary', '2026-07-01', '+', 1, 3, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (4, 'Platelets', '2025-12-20', 'Voluntary', '2025-12-15', '-', 1, 4, 3, 'Discarded');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (5, 'Whole Blood', '2026-11-01', 'Voluntary', '2026-08-01', '+', 1, 5, 3, 'Issued');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (6, 'Whole Blood', '2026-08-13', 'Voluntary', '2026-05-10', '-', 1, 2, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (7, 'Whole Blood', '2026-08-13', 'Voluntary', '2026-05-10', '+', 1, 3, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (8, 'Whole Blood', '2026-10-12', NULL, '2026-09-07', '+', 1, 6, NULL, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (9, 'Whole Blood', '2026-10-12', NULL, '2026-09-07', '+', 1, 6, NULL, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (10, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 7, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (11, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 8, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (12, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 9, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (13, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 10, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (14, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 11, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (15, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 12, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (16, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 13, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (17, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 14, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (18, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 15, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (19, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 16, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (20, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 17, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (21, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 18, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (22, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 19, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (23, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 20, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (24, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 21, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (25, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 22, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (26, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 23, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (27, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 24, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (28, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 25, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (29, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 26, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (30, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 27, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (31, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 28, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (32, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 29, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (33, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 30, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (34, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 31, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (35, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 32, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (36, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 33, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (37, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 34, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (38, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 35, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (39, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 36, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (40, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 37, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (41, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 38, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (42, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 39, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (43, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 40, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (44, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 41, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (45, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 42, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (46, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 43, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (47, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 44, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (48, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 45, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (49, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 46, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (50, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 47, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (51, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '+', 1, 48, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (52, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 49, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (53, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 50, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (54, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 51, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (55, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 52, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (56, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 53, 3, 'Available');
INSERT INTO `Blood_Unit` (`Blood_Unit_ID`, `Component_Type`, `Expiry_Date`, `Collection_Type`, `Collection_Date`, `Rh_Factor`, `Storage_ID`, `Donation_ID`, `Staff_ID`, `Status`) VALUES (57, 'Whole Blood', '2026-10-07', 'External', '2026-09-07', '-', 1, 54, 3, 'Available');

-- Data for Screening_Test
INSERT INTO `Screening_Test` (`Test_ID`, `Test_Type`, `Test_Date`, `Status`, `Result`, `Blood_Unit_ID`) VALUES (1, 'HIV/HBV/HCV/Syphilis', '2026-05-11', 'Completed', 'Negative', 1);
INSERT INTO `Screening_Test` (`Test_ID`, `Test_Type`, `Test_Date`, `Status`, `Result`, `Blood_Unit_ID`) VALUES (2, 'HIV/HBV/HCV/Syphilis', '2026-02-21', 'Completed', 'Negative', 2);
INSERT INTO `Screening_Test` (`Test_ID`, `Test_Type`, `Test_Date`, `Status`, `Result`, `Blood_Unit_ID`) VALUES (3, 'HIV/HBV/HCV/Syphilis', '2026-07-02', 'Completed', 'Negative', 3);
INSERT INTO `Screening_Test` (`Test_ID`, `Test_Type`, `Test_Date`, `Status`, `Result`, `Blood_Unit_ID`) VALUES (4, 'HIV/HBV/HCV/Syphilis', '2025-12-16', 'Completed', 'Positive', 4);
INSERT INTO `Screening_Test` (`Test_ID`, `Test_Type`, `Test_Date`, `Status`, `Result`, `Blood_Unit_ID`) VALUES (5, 'HIV/HBV/HCV/Syphilis', '2026-08-02', 'Completed', 'Negative', 5);

-- Data for Hospital_Inventory
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (1, 1, 'A+', 5, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (2, 1, 'A-', 2, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (3, 1, 'B+', 0, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (4, 1, 'O+', 9, '2026-09-07 22:33:35');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (5, 1, 'O-', 3, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (6, 1, 'AB+', 3, '2026-09-07 22:35:47');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (7, 2, 'A+', 3, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (8, 2, 'A-', 0, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (9, 2, 'B+', 7, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (10, 2, 'O+', 15, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (11, 2, 'O-', 2, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (12, 2, 'AB-', 1, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (13, 3, 'A+', 0, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (14, 3, 'B+', 2, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (15, 3, 'O+', 8, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (16, 3, 'O-', 1, '2026-09-07 21:46:40');
INSERT INTO `Hospital_Inventory` (`Inventory_ID`, `Hospital_ID`, `Blood_Group`, `Quantity`, `Last_Updated`) VALUES (17, 3, 'AB+', 5, '2026-09-07 21:46:40');

-- Data for Request
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (1, '2026-08-20', '2026-08-25', 'Pending', 'Whole Blood', 1, 'High', 'O+', 1, NULL);
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (2, '2026-08-22', '2026-08-23', 'Pending', 'Whole Blood', 3, 'Emergency', 'O+', 2, NULL);
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (3, '2026-08-21', '2026-08-24', 'Pending', 'Packed Red Cells', 2, 'High', 'O+', 3, NULL);
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (4, '2026-08-15', '2026-08-16', 'Fulfilled', 'Packed Red Cells', 1, 'Emergency', 'A-', 2, NULL);
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (5, '2026-08-22', '2026-08-26', 'Fulfilled', 'Platelets', 1, 'Routine', 'AB+', 1, NULL);
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (6, '2026-09-07', '2026-09-08', 'Fulfilled', 'Whole Blood', 1, 'Emergency', 'O+', 1, 1);
INSERT INTO `Request` (`Request_ID`, `Request_Date`, `Required_Date`, `Status`, `Component_Type`, `Qty_Required`, `Priority`, `Blood_Group`, `Hospital_ID`, `Patient_ID`) VALUES (7, '2026-09-07', '2026-09-09', 'Pending', 'Whole Blood', 4, 'Emergency', 'B-', 1, NULL);

