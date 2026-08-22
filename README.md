# Blood Bank Management System

A comprehensive web-based Blood Bank Management System built with Flask and MySQL. This system provides role-based dashboards for Staff, Hospitals, Donors, and Patients with features like smart matching, urgent request tracking, and automated inventory management.

## 🚀 Getting Started for Developers

If you are a developer (or a friend helping with the frontend), follow these steps to get the project running on your local machine.

### Prerequisites
1. **Python 3.x** installed on your system.
2. **MySQL Server** installed and running locally.
3. **Git** installed on your system.

### 1. Clone the Repository
Open your terminal and clone this repository:
```bash
git clone https://github.com/Shravya317/blood-bank-management-system.git
cd blood-bank-management-system
```

### 2. Install Dependencies
It's recommended to use a virtual environment, but you can also install the required Python packages globally:
```bash
pip install -r requirements.txt
```

### 3. Database Setup (MySQL)
You need to set up the MySQL database schema and inject the mock data:

1. Open your MySQL client (like MySQL Workbench or CLI).
2. Run the `database/schema.sql` script to create the database and tables.
3. Run the `database/mock_data.sql` script to populate the tables with initial mock data (users, blood units, etc.).

### 4. Configuration
The application connects to MySQL using the settings in `config.py`. 
You must open `config.py` in your code editor and change the `MYSQL_PASSWORD` to match **your own** local MySQL root password.

```python
class Config:
    SECRET_KEY = 'supersecretkey'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'your_mysql_password_here' # <-- CHANGE THIS
    MYSQL_DB = 'bloodbank_db'
```

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
Open your web browser and go to `http://127.0.0.1:5000/`.

---

## 🔑 Test Accounts
You can log in to the different dashboards using these mock credentials:

- **Staff / Admin:** 
  - Email: `alice.smith@bloodbank.com` 
  - Password: `admin123`
- **Hospital Rep:** 
  - License No: `LIC-10001` 
  - Password: `hosp123`
- **Donor:** 
  - Phone: `555-0201` 
  - Password: `donor123`
- **Receiver (Patient):** 
  - Phone: `555-0301` 
  - Password: `pat123`

## 🎨 Working on the Frontend
- The HTML templates are located in the `templates/` folder.
- The CSS stylesheet is located in the `static/css/style.css` file. 
- Because this uses Flask and Jinja2 templating, the HTML files use `{{ }}` and `{% %}` syntax to inject dynamic data from the database. When editing the layout or colors, you can safely modify the HTML and CSS, just be careful not to delete the Jinja tags!
