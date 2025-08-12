from django.db import models
from django.utils import timezone


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=255)
    enrollment_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.full_name} ({self.course})"
