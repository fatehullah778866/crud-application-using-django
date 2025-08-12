from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .forms import StudentForm, StudentSearchForm
import json

def student_list(request):
    """Display list of all students with search and filter functionality"""
    students = Student.objects.filter(is_active=True)
    search_form = StudentSearchForm(request.GET)
    
    # Apply search filters
    if search_form.is_valid():
        search = search_form.cleaned_data.get('search')
        department = search_form.cleaned_data.get('department')
        year = search_form.cleaned_data.get('year')
        gender = search_form.cleaned_data.get('gender')
        
        if search:
            students = students.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(student_id__icontains=search) |
                Q(email__icontains=search)
            )
        
        if department:
            students = students.filter(department=department)
        
        if year:
            students = students.filter(year=year)
        
        if gender:
            students = students.filter(gender=gender)
    
    # Pagination
    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_form': search_form,
        'total_students': students.count(),
    }
    
    return render(request, 'students/student_list.html', context)

def student_detail(request, pk):
    """Display detailed information about a specific student"""
    student = get_object_or_404(Student, pk=pk, is_active=True)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context)

def student_create(request):
    """Create a new student"""
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.full_name} created successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    
    context = {
        'form': form,
        'title': 'Add New Student',
        'button_text': 'Create Student',
    }
    return render(request, 'students/student_form.html', context)

def student_update(request, pk):
    """Update an existing student"""
    student = get_object_or_404(Student, pk=pk, is_active=True)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.full_name} updated successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
        'student': student,
        'title': 'Edit Student',
        'button_text': 'Update Student',
    }
    return render(request, 'students/student_form.html', context)

def student_delete(request, pk):
    """Delete a student (soft delete by setting is_active=False)"""
    student = get_object_or_404(Student, pk=pk, is_active=True)
    
    if request.method == 'POST':
        student.is_active = False
        student.save()
        messages.success(request, f'Student {student.full_name} deleted successfully!')
        return redirect('student_list')
    
    context = {
        'student': student,
    }
    return render(request, 'students/student_confirm_delete.html', context)

@csrf_exempt
@require_POST
def student_delete_ajax(request, pk):
    """AJAX endpoint for deleting students"""
    try:
        student = get_object_or_404(Student, pk=pk, is_active=True)
        student.is_active = False
        student.save()
        return JsonResponse({
            'success': True,
            'message': f'Student {student.full_name} deleted successfully!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)

def dashboard(request):
    """Dashboard with statistics and overview"""
    total_students = Student.objects.filter(is_active=True).count()
    department_stats = {}
    year_stats = {}
    gender_stats = {}
    
    # Department statistics
    for dept_code, dept_name in Student.DEPARTMENT_CHOICES:
        count = Student.objects.filter(department=dept_code, is_active=True).count()
        if count > 0:
            department_stats[dept_name] = count
    
    # Year statistics
    for year_code, year_name in Student.YEAR_CHOICES:
        count = Student.objects.filter(year=year_code, is_active=True).count()
        if count > 0:
            year_stats[year_name] = count
    
    # Gender statistics
    for gender_code, gender_name in Student.GENDER_CHOICES:
        count = Student.objects.filter(gender=gender_code, is_active=True).count()
        if count > 0:
            gender_stats[gender_name] = count
    
    # Recent students
    recent_students = Student.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    # Top performing students (by CGPA)
    top_students = Student.objects.filter(is_active=True, cgpa__gt=0).order_by('-cgpa')[:5]
    
    context = {
        'total_students': total_students,
        'department_stats': department_stats,
        'year_stats': year_stats,
        'gender_stats': gender_stats,
        'recent_students': recent_students,
        'top_students': top_students,
    }
    
    return render(request, 'students/dashboard.html', context)

def export_students(request):
    """Export students data (placeholder for future implementation)"""
    students = Student.objects.filter(is_active=True)
    context = {
        'students': students,
    }
    return render(request, 'students/export.html', context)
