# manbridge/student/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def student_home(request):
    # Dashboard landing for students
    return render(request, "student/dashboard.html")

@login_required
def student_attendance(request):
    # View attendance page
    return render(request, "student/attendance.html")

@login_required
def student_results(request):
    # View exam/test results
    return render(request, "student/results.html")

@login_required
def student_leave(request):
    # Apply for leave
    return render(request, "student/leave.html")
