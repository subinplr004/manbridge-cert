from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('certificate_issuer', 'Certificate Issuer'),
        ('staff', 'Teaching Staff'),
        ('sales', 'Sales & Marketing'),
        ('front_office', 'Front Office'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_pic = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        default='default-user.png'
    )

    def save(self, *args, **kwargs):
        # If we're only updating last_login (or any other field
        # but profile_pic), skip all the image logic:
        update_fields = kwargs.get('update_fields', None)
        if update_fields is not None and 'profile_pic' not in update_fields:
            return super().save(*args, **kwargs)

        # 1) Persist instance so file exists
        super().save(*args, **kwargs)

        # 2) Skip if no pic or it's the default
        default_name = 'default-user.png'
        if not self.profile_pic or self.profile_pic.name == default_name:
            return

        # 3) If the file truly doesn’t exist, reset to default:
        storage = self.profile_pic.storage
        if not storage.exists(self.profile_pic.name):
            self.profile_pic = default_name
            super().save(update_fields=['profile_pic'])
            return

        # 4) Load image
        try:
            img = Image.open(self.profile_pic.path)
        except Exception:
            try:
                img = Image.open(self.profile_pic.open())
            except Exception:
                # broken file → reset and bail
                self.profile_pic = default_name
                super().save(update_fields=['profile_pic'])
                return

        # 5) Resize if needed
        max_size = (500, 500)
        if img.width > max_size[0] or img.height > max_size[1]:
            try:
                resample = Image.Resampling.LANCZOS
            except AttributeError:
                resample = Image.LANCZOS

            img.thumbnail(max_size, resample)

            buf = BytesIO()
            img.save(buf, format='JPEG', quality=70)
            buf.seek(0)

            self.profile_pic.save(
                self.profile_pic.name,
                ContentFile(buf.read()),
                save=False
            )
            super().save(update_fields=['profile_pic'])

    def __str__(self):
        return self.username
