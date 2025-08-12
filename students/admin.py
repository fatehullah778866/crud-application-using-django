from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'student_id', 'first_name', 'last_name', 'email', 
        'course', 'year_of_study', 'gpa', 'is_active', 'created_at'
    ]
    
    list_filter = [
        'is_active', 'year_of_study', 'gender', 'course', 'created_at'
    ]
    
    search_fields = [
        'student_id', 'first_name', 'last_name', 'email', 'course'
    ]
    
    readonly_fields = ['created_at', 'updated_at', 'age']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('student_id', 'first_name', 'last_name', 'email', 
                      'phone_number', 'date_of_birth', 'gender')
        }),
        ('Academic Information', {
            'fields': ('course', 'year_of_study', 'gpa')
        }),
        ('Address Information', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('System Information', {
            'fields': ('is_active', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    list_per_page = 25
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def age(self, obj):
        return obj.age
    age.short_description = 'Age'
