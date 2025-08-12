# Register Student model in admin interface

from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "age", "enrollment_date")
    search_fields = ("first_name", "last_name", "email")
