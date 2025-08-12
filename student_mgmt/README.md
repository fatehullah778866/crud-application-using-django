# Student Management System (Django)

A simple CRUD Student Management System built with Django and SQLite.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd student_mgmt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open http://localhost:8000 in your browser.

## Features
- Add, list, view, edit, and delete students
- SQLite default database
- Basic styling in `static/css/styles.css`