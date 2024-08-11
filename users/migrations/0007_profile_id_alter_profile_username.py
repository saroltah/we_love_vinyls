from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_image'),  # or your latest migration
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]

