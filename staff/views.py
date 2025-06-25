# staff/views.py
from django.shortcuts import render

def staff_home(request):
    return render(request, "staff/dashboard.html")

def staff_take_attendance(request):
    # …your code…
    return render(request, "staff/take_attendance.html")

def staff_update_attendance(request):
    # …your code…
    return render(request, "staff/update_attendance.html")

def staff_add_result(request):
    # …your code…
    return render(request, "staff/add_result.html")

