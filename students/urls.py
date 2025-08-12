from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Student CRUD operations
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    
    # Search functionality
    path('students/search/', views.student_search, name='student_search'),
]