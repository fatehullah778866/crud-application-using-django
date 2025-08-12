from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from datetime import date

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id', 'first_name', 'last_name', 'email', 'phone',
            'date_of_birth', 'gender', 'department', 'year', 'semester',
            'cgpa', 'address', 'city', 'state', 'postal_code', 'country',
            'profile_picture', 'emergency_contact', 'emergency_contact_name'
        ]
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student ID'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'department': forms.Select(attrs={
                'class': 'form-select'
            }),
            'year': forms.Select(attrs={
                'class': 'form-select'
            }),
            'semester': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '8'
            }),
            'cgpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0.00',
                'max': '4.00',
                'step': '0.01'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Enter Address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter State'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Postal Code'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Country'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'emergency_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Emergency Contact'
            }),
            'emergency_contact_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Emergency Contact Name'
            }),
        }
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 15 or age > 100:
                raise ValidationError("Age must be between 15 and 100 years.")
        return dob
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            raise ValidationError("Phone number must contain only digits, spaces, hyphens, or plus sign.")
        return phone
    
    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if student_id:
            # Check if student_id already exists (for updates, exclude current instance)
            instance = getattr(self, 'instance', None)
            if Student.objects.filter(student_id=student_id).exclude(pk=instance.pk if instance else None).exists():
                raise ValidationError("Student ID already exists.")
        return student_id
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Check if email already exists (for updates, exclude current instance)
            instance = getattr(self, 'instance', None)
            if Student.objects.filter(email=email).exclude(pk=instance.pk if instance else None).exists():
                raise ValidationError("Email already exists.")
        return email

class StudentSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by name, ID, or email...'
        })
    )
    department = forms.ChoiceField(
        choices=[('', 'All Departments')] + Student.DEPARTMENT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    year = forms.ChoiceField(
        choices=[('', 'All Years')] + Student.YEAR_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    gender = forms.ChoiceField(
        choices=[('', 'All Genders')] + Student.GENDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )