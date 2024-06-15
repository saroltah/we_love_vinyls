from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, primary_key=True)
    slug = AutoSlugField(unique=True, populate_from='username')
    preferred_music = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/', default='../default_music_tf1fuy'
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ["-created_on"]
    
    class Meta:
        managed = True
        db_table = 'users_profile'
        