# user_acc/forms.py
from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm

class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': (
                'w-full border rounded p-2 '
                'bg-white text-gray-900 '
                'dark:bg-gray-800 dark:text-gray-100'
            ),
            'placeholder': '••••••••'
        }),
        required=False,
        help_text="Leave blank to keep your current password"
    )
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_pic', ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': (
                    'w-full border rounded p-2 '
                    'bg-white text-gray-900 '
                    'dark:bg-gray-800 dark:text-gray-100'
                )
            }),
            'last_name': forms.TextInput(attrs={
                'class': (
                    'w-full border rounded p-2 '
                    'bg-white text-gray-900 '
                    'dark:bg-gray-800 dark:text-gray-100'
                )
            }),
            'email': forms.EmailInput(attrs={
                'class': (
                    'w-full border rounded p-2 '
                    'bg-white text-gray-900 '
                    'dark:bg-gray-800 dark:text-gray-100'
                )
            }),
            'profile_pic': forms.ClearableFileInput(attrs={
                'class': (
                    'w-full text-gray-900 '
                    'dark:text-gray-100'
                )
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        new_pw = self.cleaned_data.get('password')
        if new_pw:
            user.set_password(new_pw)          # ← use set_password, not make_password
        if commit:
            user.save()
        return user


#password reset form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "id": "id_email",
            "type": "email",
            "class": (
                "w-full px-4 py-2 border rounded-lg "
                "border-gray-300 dark:border-gray-600 "
                "focus:outline-none focus:ring-2 focus:ring-primary "
                "dark:bg-gray-700 dark:text-white"
            ),
            "placeholder": "you@example.com",
            "required": True,
        })
    )

#custom set password form
from django import forms
from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": (
                "w-full px-4 py-2 border rounded-lg "
                "border-gray-300 dark:border-gray-600 "
                "focus:outline-none focus:ring-2 focus:ring-primary "
                "dark:bg-gray-700 dark:text-white"
            ),
            "placeholder": "•••••••••••••••",
        }),
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": (
                "w-full px-4 py-2 border rounded-lg "
                "border-gray-300 dark:border-gray-600 "
                "focus:outline-none focus:ring-2 focus:ring-primary "
                "dark:bg-gray-700 dark:text-white"
            ),
            "placeholder": "•••••••••••••••",
        }),
    )
