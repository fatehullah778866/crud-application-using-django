# Student Management System

A comprehensive Django-based web application for managing student records with full CRUD (Create, Read, Update, Delete) functionality.

## Features

- **Complete CRUD Operations**: Add, view, edit, and delete student records
- **Advanced Search & Filtering**: Search students by name, ID, email, course, year, and gender
- **Responsive Design**: Modern, mobile-friendly interface using Bootstrap 5
- **Comprehensive Student Profiles**: Personal, academic, and address information
- **Data Validation**: Form validation with helpful error messages
- **Admin Interface**: Django admin panel for backend management
- **Professional UI**: Clean, modern design with custom CSS styling

## Student Information Fields

- **Personal**: Student ID, Name, Email, Phone, Date of Birth, Gender
- **Academic**: Course, Year of Study, GPA
- **Address**: Full address with city, state, and ZIP code
- **System**: Creation/modification timestamps, active status

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
student_management/
├── manage.py
├── requirements.txt
├── student_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── students/
│           ├── base.html
│           ├── home.html
│           ├── student_list.html
│           ├── student_detail.html
│           ├── student_form.html
│           ├── student_confirm_delete.html
│           └── student_search.html
└── static/
    └── css/
        └── style.css
```

## Key Features

### 1. Home Dashboard
- Overview of total students
- Quick action buttons
- Recently added students list
- Statistics cards

### 2. Student List
- Paginated table view
- Quick search functionality
- Sortable columns
- Action buttons for each student

### 3. Student Details
- Comprehensive student profile view
- All personal, academic, and address information
- Quick actions sidebar
- Edit and delete options

### 4. Add/Edit Student
- Multi-section form with validation
- Real-time form validation feedback
- Auto-formatting for certain fields
- Comprehensive error handling

### 5. Advanced Search
- Multiple filter options
- Quick filter buttons
- Paginated results
- Search tips and help

### 6. Delete Confirmation
- Safe deletion with confirmation
- Shows what will be deleted
- Alternative action suggestions
- Double confirmation for safety

## Technology Stack

- **Backend**: Django 5.2.5
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0.0
- **Database**: SQLite (default, easily changeable)
- **Python**: 3.8+

## Database Model

The `Student` model includes:
- Unique student ID with validation
- Personal information fields
- Academic tracking (course, year, GPA)
- Complete address information
- System timestamps and status flags
- Built-in validation and constraints

## Customization

The application is designed to be easily customizable:
- Modify the `Student` model to add/remove fields
- Customize the CSS in `static/css/style.css`
- Add new views and templates as needed
- Extend the admin interface in `admin.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support, please open an issue in the GitHub repository or contact the development team.
