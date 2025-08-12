from django.urls import path

from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)

app_name = "students"

urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("student/create/", StudentCreateView.as_view(), name="student_create"),
    path("student/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("student/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
]