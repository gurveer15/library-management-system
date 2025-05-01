# 📚 Library Management System (CLI)

A Command Line Interface (CLI)-based Library Management System built using Python and MySQL. It allows users to manage books, issue/return them, and maintain fine records efficiently. Admin authentication is also supported.

---

## ✅ Features

- Register library members  
- Add, view, and search books  
- Issue and return books with return deadline tracking  
- Fine calculation for late returns  
- View fine payment history  
- Admin authentication using secure password input  
- Colored terminal output for better UX (via `colorama`)  

---

## 🛠️ Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/gurveer15/library-management-system.git
cd library-management-system
```

### 2. Install required Python packages:
```bash
pip install mysql-connector-python colorama
```
### 3. Set up MySQL Database:
Create a database and tables using the sb.sql file.
Configure your DB credentials in config.py.

### 4. Run the application:
```bash
python main.py
```
### 🗂️ File Structure

- `main.py`: Entry point for admin or member actions  
- `admin.py`: Admin-specific operations like issuing/returning books  
- `member.py`: Member operations like registration and browsing books  
- `database.py`: Connection handling  
- `config.py`: DB configuration settings  
- `sb.sql`: SQL schema for setting up the database  


### License

This project is licensed under the MIT License - see the LICENSE file for details.