from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
import os

# Create your views here.
def login_redirect(request):
    role = request.user.role
    if role == 'admin':
        return redirect('admin_dashboard')
    elif role == 'certificate_issuer':
        return redirect('certificate_dashboard')
    elif role == 'staff':
        return redirect('staff_dashboard')
    elif role == 'sales':
        return redirect('sales_dashboard')
    elif role == 'front_office':
        return redirect('front_office_dashboard')
    elif role == 'student':
        return redirect('student_dashboard')


def custom_login(request):
    # Only accept POST here – any GET or other method goes back to landing
    if request.method != "POST":
        return redirect("landing")

    # Grab credentials from the POST body
    username = request.POST.get("username")
    password = request.POST.get("password")

    # Try to authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Log them in and send to the correct dashboard
        login(request, user)
        return redirect("role_redirect")
    else:
        # Bad creds → flash an error and go back to the landing page
        messages.error(request, "Invalid username or password")
        return redirect("landing")

def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            # Save the updated profile (and password if provided)
            form.save()

            # Notify them, then log out
            messages.success(request, "Profile updated — please log in again.")
            logout(request)

            # Redirect to your login page
            return redirect("login")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "user_acc/profile_update.html", {"form": form})


@login_required
def role_redirect(request):
    return render(request, 'role_dashboard.html')  # universal dashboard

