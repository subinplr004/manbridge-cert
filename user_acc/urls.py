from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('role-redirect/', views.role_redirect, name='role_redirect'),
    path('profile-update/', views.profile_update, name='profile_update'),

    path('role-redirect/', views.role_redirect, name='role_redirect'),
    # # Dummy Dashboards
    # path('admin/dashboard/', views.dummy_view, name='admin_dashboard'),
    # path('certificate/dashboard/', views.dummy_view, name='certificate_dashboard'),
    # path('staff/dashboard/', views.dummy_view, name='staff_dashboard'),
    # path('sales/dashboard/', views.dummy_view, name='sales_dashboard'),
    # path('front-office/dashboard/', views.dummy_view, name='front_office_dashboard'),
    # path('student/dashboard/', views.dummy_view, name='student_dashboard'),
    
]
