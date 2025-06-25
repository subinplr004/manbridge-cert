# certificate/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def certificate_dashboard(request):
    """
    Landing page for certificate-issuer users.
    Show summary stats or recent activity.
    """
    return render(request, "certificate/dashboard.html")


@login_required
def issue_certificate(request):
    """
    Form for issuing a new certificate.
    On POST, validate and create a certificate record.
    """
    if request.method == "POST":
        # TODO: process form data, create certificate...
        messages.success(request, "Certificate issued successfully!")
        return redirect("certificate:dashboard")

    return render(request, "certificate/issue_certificate.html")


@login_required
def verify_certificate(request):
    """
    Page to lookup and verify a certificate code/serial.
    """
    if request.method == "POST":
        code = request.POST.get("code", "").strip()
        # TODO: lookup Certificate.objects.filter(code=code)...
        found = False  # replace with real check
        if found:
            messages.success(request, f"Certificate {code} is valid.")
        else:
            messages.error(request, f"No certificate found for {code}.")
        return redirect("certificate:verify")

    return render(request, "certificate/verify_certificate.html")
