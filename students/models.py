from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('BT', 'Biotechnology'),
        ('CH', 'Chemical Engineering'),
        ('PH', 'Physics'),
        ('MA', 'Mathematics'),
        ('EN', 'English'),
        ('HI', 'History'),
        ('EC', 'Economics'),
    ]
    
    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    ]
    
    # Basic Information
    student_id = models.CharField(max_length=20, unique=True, verbose_name="Student ID")
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    
    # Academic Information
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES, verbose_name="Department")
    year = models.IntegerField(choices=YEAR_CHOICES, verbose_name="Year")
    semester = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        verbose_name="Semester"
    )
    cgpa = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(4.00)],
        default=0.00,
        verbose_name="CGPA"
    )
    
    # Address Information
    address = models.TextField(verbose_name="Address")
    city = models.CharField(max_length=50, verbose_name="City")
    state = models.CharField(max_length=50, verbose_name="State")
    postal_code = models.CharField(max_length=10, verbose_name="Postal Code")
    country = models.CharField(max_length=50, default="India", verbose_name="Country")
    
    # Additional Information
    profile_picture = models.ImageField(
        upload_to='student_photos/',
        blank=True,
        null=True,
        verbose_name="Profile Picture"
    )
    emergency_contact = models.CharField(max_length=15, verbose_name="Emergency Contact")
    emergency_contact_name = models.CharField(max_length=100, verbose_name="Emergency Contact Name")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    # Status
    is_active = models.BooleanField(default=True, verbose_name="Active Status")
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['student_id']
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
    def get_department_display_name(self):
        return dict(self.DEPARTMENT_CHOICES)[self.department]
    
    def get_year_display_name(self):
        return dict(self.YEAR_CHOICES)[self.year]
