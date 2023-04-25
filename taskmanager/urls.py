from django.urls import path
from .views import generate_student, generate_students

urlpatterns = [
    path('generate-student/', generate_student, name='generate_student'),
    path('generate-students/', generate_students, name='generate_students'),
]
