# Generated by Django 3.2.4 on 2024-08-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_alter_record_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='condition',
            field=models.CharField(choices=[('good', 'Good'), ('new', 'New'), ('used', 'Used')], default='good', max_length=9),
        ),
    ]
