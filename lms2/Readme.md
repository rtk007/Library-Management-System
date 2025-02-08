# LMS2 - Library Management System

This is **LMS2*, a Library Management System that uses QuaggaJS for barcode-based authentication and a Django backend for data management. It facilitates efficient handling of library operations such as book borrowing, returning, and member management.

## Features
- Barcode-based authentication using QuaggaJS
- Book borrowing and return management
- Member registration and management
- Admin dashboard for library operations
- Templates for UI rendering
- Static files for styling

## Project Structure
```
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
```

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd LMS2
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *If `requirements.txt` is not available, install Django and QuaggaJS dependencies manually:*
   ```bash
   pip install django
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up a username, email, and password.

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/` to see the application.

## Barcode Authentication Setup
- Integrate QuaggaJS in your frontend templates located in `libraryapp/templates/`.
- Use barcode scanners to authenticate users for book borrowing and returning.

## Usage
- Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
- Manage books and members through the web interface.
- Authenticate members using barcode scanning.

## Directory Details
- **`LibMS/`:** Contains project-level settings and configurations.
- **`libraryapp/`:** The main app managing books, members, forms, views, templates, and static files.
- **`db.sqlite3`:** The SQLite database file storing application data.

## Customization
- To modify the UI, update files in `libraryapp/templates/` and `libraryapp/static/`.
- For backend logic, edit `libraryapp/views.py`, `libraryapp/models.py`, and `libraryapp/forms.py`.
- For barcode authentication, modify the QuaggaJS integration in the templates.

In the env file add your email backend id and required email fields
## Contact
For any inquiries or support, please contact Ratik Krishna M P at ratikkrishna15@gmail.com.

