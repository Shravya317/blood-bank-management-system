# Blood Bank Management System

A relational database management system for blood donation tracking, inventory storage, safety screening tests, hospital request fulfillment, and compatibility matching.

## ER Diagram

[![Blood Bank Management System ER Diagram](./BLOODBANK.drawio.svg)](./BLOODBANK.drawio.svg)

> **Note**: Click the diagram above to view the full-resolution vector image in a new tab.

---

## Database Architecture & Entities

The system models **10 primary entities** and **1 compatibility mapping table**:

1. **Hospital**: Tracks receiving medical centers and license credentials.
2. **Staff**: Medical staff, technicians, and administrators.
3. **Storage**: Physical refrigerators, freezers, and agitators.
4. **Donor**: Profiles, blood groups, and donation eligibility states.
5. **Patient**: Recipients, clinical conditions, and registered staff references.
6. **Donation**: Log of blood collection events.
7. **Blood_Unit**: Inventory bags (RBCs, Platelets, FFP, Cryo) with expiry tracking.
8. **Screening_Test**: Safety validation (infectious disease screening).
9. **Request**: Hospital order placement tracking priority and status.
10. **Issue**: Fulfillment dispatches connecting inventory units to requests.
11. **Donor_Patient_Match**: Direct compatibility matrix matching donor-recipient pairs.

---

## How to Run in Visual Studio Code

### Step 1: Open Project Workspace
Open Visual Studio Code and navigate to the project directory.

### Step 2: Run Initializer Script
Open your VSC integrated terminal (`Ctrl + ~`) and execute:

```bash
python app.py
```

This will automatically:
- Create the SQLite database (`blood_bank.db`).
- Build all 11 tables with foreign key constraints.
- Seed the database with comprehensive mock records.
- Output all raw tables and operational JOIN reports.
