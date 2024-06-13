from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, primary_key=True)
    slug = AutoSlugField(unique=True, populate_from='username')
    preferred_music = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ["-created_on"]
