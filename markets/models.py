from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Market(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    date = models.DateField()
    start = models.TimeField(default='12:00')
    end = models.TimeField()
    description = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"in {self.city} by {self.organizer}"
