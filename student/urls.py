# student/urls.py
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("home/", views.student_home,            name="home"),
    path("attendance/", views.student_attendance, name="attendance"),
    path("results/",    views.student_results,    name="results"),
    path("leave/",      views.student_leave,      name="leave"),
]
