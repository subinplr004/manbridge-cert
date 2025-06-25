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
        default='profiles/default-user.png'
    )

    def save(self, *args, **kwargs):
        # 1) First save so file exists
        super().save(*args, **kwargs)

        # 2) Don't process the default placeholder
        if not self.profile_pic or self.profile_pic.name == 'profiles/default-user.png':
            return

        # Try to open via filesystem; fall back to storage
        try:
            img = Image.open(self.profile_pic.path)
        except (AttributeError, ValueError, OSError):
            self.profile_pic.open()
            img = Image.open(self.profile_pic)

        # 3) Only resize if larger than our max
        max_size = (500, 500)
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size, Image.ANTIALIAS)

            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=70)
            buffer.seek(0)

            # 4) Overwrite the file in-place (no extra DB save yet)
            self.profile_pic.save(
                self.profile_pic.name,
                ContentFile(buffer.read()),
                save=False
            )

            # 5) Persist the updated image field
            super().save(update_fields=['profile_pic'])

    def __str__(self):
        return self.username
