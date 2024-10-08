from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from='username')
    preferred_music = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/', default='../option_yellow_yktljb', blank=True
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ["-created"]
