# Generated by Django 3.2.4 on 2024-08-12 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_rename_track_list_record_tracklist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='tracklist',
            new_name='track_list',
        ),
    ]