from django.db import models

# Create your models here.

# Student model for CRUD operations


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-enrollment_date"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
