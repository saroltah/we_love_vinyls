# Generated by Django 3.2.14 on 2024-06-30 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='created',
        ),
    ]
