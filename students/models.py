from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ]
    
    # Personal Information
    student_id = models.CharField(
        max_length=20, 
        unique=True,
        validators=[RegexValidator(r'^[A-Z0-9]+$', 'Student ID must contain only uppercase letters and numbers')]
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')]
    )
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Academic Information
    course = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=1, choices=YEAR_CHOICES)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    # Address Information
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    
    # System Information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
