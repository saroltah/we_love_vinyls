# Generated by Django 4.2.10 on 2024-06-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../option_purple_wikcab', upload_to='images/'),
        ),
    ]
