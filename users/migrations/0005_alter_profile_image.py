# Generated by Django 4.2.10 on 2024-06-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(choices=[('../option_purple_wikcab', 'Purple long hair'), ('../option_green_cup_xr6udp', 'Green cup short hair'), ('../option_brown_cup_ulh7yf', 'Brown cup long hair'), ('../option_yellow_yktljb', 'Yellow long hair'), ('../option_pink_b4oxol', 'Pink long hair'), ('../option_blue_z6v4v7', 'Blue short hair'), ('../option_green_aqa4tn', 'Green short hair')], default='../option_purple_wikcab', upload_to='images/'),
        ),
    ]
