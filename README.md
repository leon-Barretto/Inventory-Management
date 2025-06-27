# Inventory Management System - Flask Application

## Project Description

This is a web-based Inventory Management System built using Python and Flask.  
The system allows businesses to:

- Add new inventory items.
- View and manage existing inventory.
- Record sales and automatically update stock levels.
- Visualize current stock levels using a dashboard with Chart.js.

The application solves a common business problem where small businesses often struggle to track and update inventory efficiently. This tool helps automate and simplify that process.

---

## Features

- Add inventory items (name, category, price, stock)
- View full inventory list
- Record sales transactions (reduce stock)
- Automatic stock updates after sales
- Dynamic data visualization (Chart.js dashboard)
- File-based storage using JSON (no external database required)

---

## Technologies Used

- Python 3
- Flask
- HTML / Jinja2 Templates
- JSON for file-based database
- Chart.js for data visualization

---

## Project Structure
```
/Inventory-Management-System/
│
├── app.py
├── inventory.json
├── README.md
├── Report.pdf  (optional)
└── /templates/
    ├── index.html
    ├── inventory.html
    ├── add_item.html
    ├── sales.html
    └── dashboard.html
```

---

## Installation and Running the Application

### Install Python 3  
Ensure Python 3 is installed on your system.

### Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

### Install Flask  
Open terminal or command prompt and run:
pip3 install flask

### Run the Flask application
Ensure the virtual environment is activated.
flask run

### Access the app by opening your web browser and going to:
http://127.0.0.1:5000/
