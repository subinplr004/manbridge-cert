# staff/urls.py
from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path("home/",               views.staff_home,            name="home"),
    path("attendance/take/",    views.staff_take_attendance, name="take"),
    path("attendance/update/",  views.staff_update_attendance, name="update"),
    path("result/add/",         views.staff_add_result,      name="add_result"),
]
