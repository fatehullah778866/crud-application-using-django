# Student Management System

A comprehensive full-stack Django CRUD application for managing student information with a modern, responsive web interface.

## 🚀 Features

### Core Functionality
- **Complete CRUD Operations**: Create, Read, Update, Delete student records
- **Advanced Search & Filtering**: Search by name, ID, email, department, year, and gender
- **Dashboard Analytics**: Visual statistics with charts and graphs
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **File Upload**: Profile picture upload functionality
- **Data Export**: Export student data in CSV/Excel formats
- **Admin Interface**: Django admin panel for data management

### Student Information Management
- **Personal Details**: Name, ID, email, phone, date of birth, gender
- **Academic Information**: Department, year, semester, CGPA
- **Address Details**: Complete address with city, state, postal code, country
- **Emergency Contact**: Emergency contact name and number
- **Profile Pictures**: Student photo upload and display
- **System Tracking**: Creation and update timestamps

### User Interface Features
- **Modern Dashboard**: Statistics cards, charts, and overview
- **Interactive Tables**: Sortable, paginated student lists
- **Form Validation**: Real-time client-side and server-side validation
- **AJAX Operations**: Smooth delete operations without page refresh
- **Responsive Navigation**: Mobile-optimized navigation menu
- **Alert System**: Success/error message notifications

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (default), supports PostgreSQL, MySQL
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Charts**: Chart.js
- **Image Processing**: Pillow
- **Form Styling**: Django Crispy Forms

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd student-management-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Default admin credentials:
- Username: `admin`
- Password: `admin123`

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
- **Main Application**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

## 📁 Project Structure

```
student_management_system/
├── manage.py
├── requirements.txt
├── README.md
├── student_management_system/
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
│   └── views.py
├── templates/
│   ├── base.html
│   └── students/
│       ├── dashboard.html
│       ├── student_list.html
│       ├── student_detail.html
│       ├── student_form.html
│       ├── student_confirm_delete.html
│       └── export.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── media/
│   └── student_photos/
└── db.sqlite3
```

## 🎯 Usage Guide

### Dashboard
- View overall statistics and analytics
- Access recent students and top performers
- Navigate to different sections

### Student Management
1. **Add New Student**: Click "Add New Student" button
2. **View Students**: Browse the student list with search/filter options
3. **Edit Student**: Click the edit icon on any student record
4. **Delete Student**: Use the delete button (soft delete - marks as inactive)
5. **View Details**: Click on student name or view icon for detailed information

### Search and Filter
- Use the search bar to find students by name, ID, or email
- Filter by department, year, or gender
- Combine multiple filters for precise results

### Data Export
- Navigate to Export page
- Select export format (CSV/Excel)
- Choose fields to include
- Apply filters if needed
- Download the exported file

## 🔧 Configuration

### Database Configuration
The application uses SQLite by default. To use other databases, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
Static files are configured for development. For production:

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### Media Files
Profile pictures are stored in `media/student_photos/`. Ensure the directory is writable.

## 🎨 Customization

### Styling
- Modify `static/css/style.css` for custom styling
- Update Bootstrap theme colors in CSS variables
- Add custom animations and effects

### Templates
- Edit templates in `templates/students/` directory
- Modify base template for global changes
- Add new pages by creating new template files

### JavaScript
- Enhance functionality in `static/js/main.js`
- Add new interactive features
- Implement additional AJAX operations

## 🔒 Security Features

- CSRF protection on all forms
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- Secure file upload handling

## 📊 API Endpoints

The application includes RESTful endpoints:

- `GET /` - Dashboard
- `GET /students/list/` - Student list with search/filter
- `GET /students/create/` - Create student form
- `POST /students/create/` - Create student
- `GET /students/<id>/` - Student details
- `GET /students/<id>/edit/` - Edit student form
- `POST /students/<id>/edit/` - Update student
- `POST /students/<id>/delete/` - Delete student
- `POST /students/<id>/delete-ajax/` - AJAX delete
- `GET /students/export/` - Export page

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up a production database
4. Configure static file serving
5. Set up environment variables for sensitive data

### Environment Variables
```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
export ALLOWED_HOSTS='your-domain.com'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Version History

- **v1.0.0** - Initial release with full CRUD functionality
- Features: Dashboard, Student Management, Search/Filter, Export

## 📞 Contact

- **Developer**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [your-github-profile]

---

**Note**: This is a development version. For production use, ensure proper security measures and database configuration.
