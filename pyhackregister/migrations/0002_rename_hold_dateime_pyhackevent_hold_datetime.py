# Generated by Django 4.2.17 on 2025-01-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyhackregister', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pyhackevent',
            old_name='hold_dateime',
            new_name='hold_datetime',
        ),
    ]
