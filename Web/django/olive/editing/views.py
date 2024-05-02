from django.shortcuts import render
from django.shortcuts import render
from .models import Student
# Create your views here.
def portfolio_details(request):
    return render(request, 'portfolio-details.html')
def insert_students(request):
    return render(request, 'insertstudents.html')
def students(request):
    student = Student.objects.all()
    return render(request, 'student.html', {"students": student})
