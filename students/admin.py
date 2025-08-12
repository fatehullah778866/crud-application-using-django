from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'student_id', 'full_name', 'email', 'department', 'year', 
        'semester', 'cgpa', 'is_active', 'created_at'
    ]
    list_filter = [
        'department', 'year', 'semester', 'gender', 'is_active', 
        'created_at', 'updated_at'
    ]
    search_fields = [
        'student_id', 'first_name', 'last_name', 'email', 'phone'
    ]
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'student_id', 'first_name', 'last_name', 'email', 'phone',
                'date_of_birth', 'gender', 'profile_picture'
            )
        }),
        ('Academic Information', {
            'fields': (
                'department', 'year', 'semester', 'cgpa'
            )
        }),
        ('Address Information', {
            'fields': (
                'address', 'city', 'state', 'postal_code', 'country'
            )
        }),
        ('Emergency Contact', {
            'fields': (
                'emergency_contact', 'emergency_contact_name'
            )
        }),
        ('System Information', {
            'fields': (
                'is_active', 'created_at', 'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Full Name'
    full_name.admin_order_field = 'first_name'
