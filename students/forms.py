from django import forms
from django.core.exceptions import ValidationError
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id', 'first_name', 'last_name', 'email', 'phone_number',
            'date_of_birth', 'gender', 'course', 'year_of_study', 'gpa',
            'address', 'city', 'state', 'zip_code', 'is_active'
        ]
        
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student ID (e.g., STU001)'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1234567890'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course name'
            }),
            'year_of_study': forms.Select(attrs={
                'class': 'form-control'
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'max': '4.00',
                'placeholder': '0.00'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter full address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter state'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ZIP code'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        
        labels = {
            'student_id': 'Student ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'course': 'Course',
            'year_of_study': 'Year of Study',
            'gpa': 'GPA',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'ZIP Code',
            'is_active': 'Active Status'
        }
    
    def clean_student_id(self):
        student_id = self.cleaned_data['student_id'].upper()
        
        # Check if student_id already exists (excluding current instance if updating)
        if self.instance.pk:
            if Student.objects.filter(student_id=student_id).exclude(pk=self.instance.pk).exists():
                raise ValidationError("A student with this ID already exists.")
        else:
            if Student.objects.filter(student_id=student_id).exists():
                raise ValidationError("A student with this ID already exists.")
        
        return student_id
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        
        # Check if email already exists (excluding current instance if updating)
        if self.instance.pk:
            if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError("A student with this email already exists.")
        else:
            if Student.objects.filter(email=email).exists():
                raise ValidationError("A student with this email already exists.")
        
        return email
    
    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        if gpa is not None and (gpa < 0 or gpa > 4.00):
            raise ValidationError("GPA must be between 0.00 and 4.00.")
        return gpa
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        # Capitalize first letter of names
        if first_name:
            cleaned_data['first_name'] = first_name.title()
        if last_name:
            cleaned_data['last_name'] = last_name.title()
        
        return cleaned_data