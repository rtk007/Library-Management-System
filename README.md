LMS2 - Library Management System
This is LMS2, a Library Management System that uses QuaggaJS for barcode-based authentication and a Django backend for data management. It facilitates efficient handling of library operations such as book borrowing, returning, and member management.

Features
Barcode-based authentication using QuaggaJS
Book borrowing and return management
Member registration and management
Admin dashboard for library operations
Templates for UI rendering
Static files for styling
Project Structure
markdown
Copy
Edit
LMS2/  
├── db.sqlite3  
├── manage.py  
├── LMS2/  
│   ├── __init__.py  
│   ├── asgi.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
└── libraryapp/  
    ├── __init__.py  
    ├── admin.py  
    ├── apps.py  
    ├── forms.py  
    ├── migrations/  
    ├── models.py  
    ├── static/  
    ├── templates/  
    ├── tests.py  
    ├── urls.py  
    └── views.py  
Prerequisites
Ensure you have the following installed:

Python 3.x
pip (Python package installer)
virtualenv (optional but recommended)
Setup Instructions
Clone the Repository:

git clone <repository-url>
cd LMS2

Create and Activate Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:

pip install -r requirements.txt
If requirements.txt is not available, install Django and QuaggaJS dependencies manually:

pip install django

Apply Migrations:
python manage.py migrate

Create Superuser (for admin access):

python manage.py createsuperuser
Follow the prompts to set up a username, email, and password.

Run the Development Server:

python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to see the application.

SMTP Setup:
Use a two-factor authenticated mail ID and get the hashed password from the service provider. Use a .env file to store them securely and reference them in settings.py.

Barcode Authentication Setup
Integrate QuaggaJS in your frontend templates located in libraryapp/templates/.
Use barcode scanners to authenticate users for book borrowing and returning.
Usage
Access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.
Manage books and members through the web interface.
Authenticate members using barcode scanning.
Directory Details
LMS2/: Contains project-level settings and configurations.
libraryapp/: The main app managing books, members, forms, views, templates, and static files.
db.sqlite3: The SQLite database file storing application data.
Customization
To modify the UI, update files in libraryapp/templates/ and libraryapp/static/.
For backend logic, edit libraryapp/views.py, libraryapp/models.py, and libraryapp/forms.py.
For barcode authentication, modify the QuaggaJS integration in the templates.
Security Note
Store sensitive credentials (such as email backend credentials) in a .env file.
Ensure proper user authentication to prevent unauthorized access.
Contact
For any inquiries or support, please contact Ratik Krishna M P at ratikkrishna15@gmail.com.

Developed By
This project was entirely designed, developed, and implemented by Ratik Krishna M P as part of a team collaboration. While teammates contributed to discussions, research, and documentation, the complete backend and frontend development were handled by me.

