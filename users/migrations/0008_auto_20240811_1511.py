# Generated by Django 3.2.4 on 2024-08-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_id_alter_profile_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='created_on',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../option_yellow_yktljb', upload_to='images/'),
        ),
    ]
