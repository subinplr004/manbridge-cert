# manbridge/main_admin/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from core.views import landing
from django.contrib.auth import views as auth_views
from user_acc.forms import MyPasswordResetForm,CustomSetPasswordForm

urlpatterns = [
    # 1) Override admin’s logout (GET) before admin.site.urls
    path(
        'admin/logout/',
        LogoutView.as_view(next_page='/admin/login/'),
        name='admin_logout'
    ),
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),

    # 4) Your own account views (login, logout, profile-update, role-redirect, etc.)
    path('accounts/', include('user_acc.urls')),

    # 5) Django’s built-in auth URLs for:
    path(
      "accounts/password_reset/",
      auth_views.PasswordResetView.as_view(form_class=MyPasswordResetForm),
      name="password_reset",
    ),
    path(
      "accounts/password_reset/done/",
      auth_views.PasswordResetDoneView.as_view(),
      name="password_reset_done",
    ),
    path(
      'accounts/reset/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(
        form_class=CustomSetPasswordForm,
        template_name='registration/password_reset_confirm.html'
      ),
      name='password_reset_confirm'
    ),
    path('accounts/', include('django.contrib.auth.urls')),


    # 6) Other apps, each in its own namespace
    path('staff/',       include('staff.urls',       namespace='staff')),
    path('student/',     include('student.urls',     namespace='student')),
    path('certificate/', include('certificate.urls', namespace='certificate')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
