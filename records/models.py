from django.db import models
from django.utils import timezone
#from users.models import Profile
from autoslug import AutoSlugField


class Record(models.Model):
    #uploader = models.ForeignKey(Profile, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    track_list = models.TextField(default='')
    year = models.IntegerField
    created_on = models.DateTimeField(auto_now_add=True)
    CONDITION_CHOICES = (
        ("New", "New"),
        ("Good", "Good"),
        ("Used", "Used"),
    )
    condition = models.CharField(max_length=9,
                            choices=CONDITION_CHOICES,
                            default="Used")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"