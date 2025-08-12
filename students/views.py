from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Student.objects.filter(is_active=True)
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(student_id__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(course__icontains=search_query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Student created successfully!')
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully!')
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Student deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Function-based views for additional functionality
def home(request):
    """Home page view"""
    total_students = Student.objects.filter(is_active=True).count()
    recent_students = Student.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    context = {
        'total_students': total_students,
        'recent_students': recent_students,
    }
    return render(request, 'students/home.html', context)

def student_search(request):
    """Advanced search view"""
    students = Student.objects.filter(is_active=True)
    
    # Get search parameters
    search_query = request.GET.get('search', '')
    course_filter = request.GET.get('course', '')
    year_filter = request.GET.get('year', '')
    gender_filter = request.GET.get('gender', '')
    
    # Apply filters
    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(student_id__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    if course_filter:
        students = students.filter(course__icontains=course_filter)
    
    if year_filter:
        students = students.filter(year_of_study=year_filter)
    
    if gender_filter:
        students = students.filter(gender=gender_filter)
    
    # Pagination
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique courses for filter dropdown
    courses = Student.objects.values_list('course', flat=True).distinct()
    
    context = {
        'students': page_obj,
        'search_query': search_query,
        'course_filter': course_filter,
        'year_filter': year_filter,
        'gender_filter': gender_filter,
        'courses': courses,
        'year_choices': Student.YEAR_CHOICES,
        'gender_choices': Student.GENDER_CHOICES,
    }
    
    return render(request, 'students/student_search.html', context)
