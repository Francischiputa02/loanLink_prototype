# Generated by Django 5.0.3 on 2024-03-27 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_doctor',
            new_name='is_agent',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_paitent',
            new_name='is_client',
        ),
    ]
