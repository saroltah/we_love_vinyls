from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from records.models import Record


class Comment(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='')
    commented_record = models.ForeignKey(Record, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_on"]
    

    def __str__(self):
        return f"{self.content}"