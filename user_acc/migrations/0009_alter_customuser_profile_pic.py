# Generated by Django 5.2.3 on 2025-06-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_acc', '0008_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profiles/default-user.png', null=True, upload_to='profiles/'),
        ),
    ]
