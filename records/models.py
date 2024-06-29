from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Record(models.Model):
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='')
    track_list = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    CONDITION_CHOICES = (
        ("New", "New"),
        ("Good", "Good"),
        ("Used", "Used"),
    )
    condition = models.CharField(max_length=9,
                            choices=CONDITION_CHOICES,
                            default="Used")
    image = models.ImageField(
        upload_to='images/', default='../default_record_ibxfab'
    )

    released =  models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ["-created_on"]
    
    class Meta:
        managed = True
        db_table = 'records_record'

    def __str__(self):
        return f"{self.title}"