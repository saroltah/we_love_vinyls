# Generated by Django 4.2.10 on 2024-06-17 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_alter_profile_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='member',
        ),
    ]