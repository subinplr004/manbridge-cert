# certificate/urls.py
from django.urls import path
from . import views

app_name = "certificate"

urlpatterns = [
    # Dashboard for certificate issuers
    path("", views.certificate_dashboard, name="dashboard"),
    # Issue a new certificate
    path("issue/", views.issue_certificate, name="issue"),
    # Verify an existing certificate
    path("verify/", views.verify_certificate, name="verify"),
]
