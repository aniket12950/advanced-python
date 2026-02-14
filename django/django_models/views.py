from django.shortcuts import render
from .models import Student, Course

def home(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'django_models/home.html', {'students': students, 'courses': courses})
