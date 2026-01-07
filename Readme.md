🎟️ Technical Event Management System
A robust Django web application designed for Axciom Consulting to streamline technical event equipment rentals, vendor coordination, and order tracking.

📑 Table of Contents
Features

Prerequisites

Installation & Setup

User Guide

Project Structure

✨ Features
User Portal: A dynamic landing page to browse technical equipment by category.

Cart System: Seamlessly add items to a cart and review before checkout.

Order Tracking: Real-time status updates for bookings (Pending, Approved, etc.).

Admin Dashboard: Full control over Vendors, Items, and Order state changes.

Payment Integration: Support for Cash and UPI payment selection during checkout.

🛠 Prerequisites
Before running this project, ensure you have:

Python 3.10+ installed on your system.

pip (Python package manager).

A virtual environment tool (venv).

🚀 Installation & Setup
Clone the Repository

Bash

git clone https://github.com/PAYALTIWARI11/Axciom-Consulting.git
cd "Axciom consulting"
Create and Activate Virtual Environment

Bash

python -m venv venv
# On Windows:
.\venv\Scripts\activate
Install Dependencies

Bash

pip install -r requirements.txt
Prepare the Database

Bash

python manage.py makemigrations
python manage.py migrate
Create an Admin Account To access the vendor and order management dashboard:

Bash

python manage.py createsuperuser
Start the Development Server

Bash

python manage.py runserver
Access the site at: http://127.0.0.1:8000/

📖 User Guide
Accessing the Web Pages
Portal: http://127.0.0.1:8000/ — Main equipment gallery.

Cart: http://127.0.0.1:8000/cart/ — Review selected items.

Status: http://127.0.0.1:8000/status/ — Track your orders.

Admin: http://127.0.0.1:8000/admin/ — Manage backend data.

Managing Vendors & Status
Log in to the Admin panel using your superuser credentials.

Use the Vendors section to add new suppliers.

Use the Orders section to change an order status from "Pending" to "Approved" to update the user's status page.

📂 Project Structure
core/: Contains the main application logic, including models for Vendors, Items, and Orders, as well as the HTML templates.

event_config/: Project-level settings and the main URL routing configuration.

static/: CSS files for styling the portal and components.

db.sqlite3: Local database file (created after migrations).

Final Steps to Update GitHub:
After you create this file in VS Code:

Save the file.

Run these commands in your terminal:

Bash

git add README.md
git commit -m "Add professional README"
git push origin main
