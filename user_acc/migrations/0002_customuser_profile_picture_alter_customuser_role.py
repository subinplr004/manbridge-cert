# Generated by Django 5.2.3 on 2025-06-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_acc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('certificate_issuer', 'Certificate Issuer'), ('staff', 'Teaching Staff'), ('sales', 'Sales & Marketing'), ('front_office', 'Front Office'), ('student', 'Student')], max_length=20),
        ),
    ]
