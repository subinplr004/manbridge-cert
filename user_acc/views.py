from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            # Optional: Check if profile picture exists
            if user.profile_pic:
                try:
                    if not user.profile_pic.storage.exists(user.profile_pic.name):
                        user.profile_pic = None
                        user.save()
                except Exception:
                    user.profile_pic = None
                    user.save()

            login(request, user)
            return redirect('role_redirect')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'user_acc/login.html')


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile_update(request):
    user = request.user

    # Safety check for broken profile picture
    if user.profile_pic and not user.profile_pic.storage.exists(user.profile_pic.name):
        user.profile_pic = None
        user.save()

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)
            if form.cleaned_data['password']:
                profile.password = make_password(form.cleaned_data['password'])
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_update')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'user_acc/profile_update.html', {'form': form})


@login_required
def role_redirect(request):
    return render(request, 'role_dashboard.html')  # universal dashboard

