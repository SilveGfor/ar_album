from django.urls import path

from .views import GetStudent, GetAllStudents, CreateStudent

urlpatterns = [
    path('get_student', GetStudent.as_view()),
    path('create_student', CreateStudent.as_view()),
    path('get_all_students', GetAllStudents.as_view()),
]
