from django.db import models
from django.contrib.auth.models import User
from records.models import Record
from markets.models import Market


class Like(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='like')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['member', 'liked_record']

    def __str__(self):
        return f'{self.member} likes {self.liked_record}'

class Attendance(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    attended_market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='attendance')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['member', 'attended_market']

    def __str__(self):
        return f'{self.member} attends on {self.attended_market}'