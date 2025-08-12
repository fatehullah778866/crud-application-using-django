from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'email',
            'age',
            'course',
            'enrollment_date',
        ]