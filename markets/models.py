from django.db import models
from django.utils import timezone
from users.models import Profile


class Market(models.Model):
    organizer = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"in {self.city} by {self.organizer}"