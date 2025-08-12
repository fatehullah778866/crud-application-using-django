# Generic class-based views for Student CRUD operations

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"


class StudentCreateView(CreateView):
    model = Student
    fields = ["first_name", "last_name", "email", "age"]
    template_name = "students/student_form.html"
    success_url = reverse_lazy("students:student_list")


class StudentUpdateView(UpdateView):
    model = Student
    fields = ["first_name", "last_name", "email", "age"]
    template_name = "students/student_form.html"
    success_url = reverse_lazy("students:student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("students:student_list")
