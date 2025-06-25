from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'password']
        profile_pic = forms.ImageField(required=False)