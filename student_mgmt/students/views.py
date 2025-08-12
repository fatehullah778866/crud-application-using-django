from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/student_list.html'
    ordering = ['full_name']


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
