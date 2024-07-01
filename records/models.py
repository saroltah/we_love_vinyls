from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Record(models.Model):
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    GENRE_CHOICES = (
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Blues", "Blues"),
        ("Country", "Country"),
        ("Electronic", "Electronic"),
        ("Punk", "Punk"),
        ("Classical", "Classical"),
        ("Alternative Rock", "Alternative Rock"),
        ("Progressive Rock", "Progressive Rock"),
        ("Folk music", "Folk music"),
        ("Synth-pop", "Synth-pop"),
        ("Hip-hop", "Hip-hop"),
        ("Jazz", "Jazz"),
        ("Funk", "Funk"),
        ("Reggae", "Reggae"),
        ("Disco", "Disco"),
        ("Soul", "Soul"),
        ("Dance", "Dance"),
        ("Ska", "Ska"),
        ("Indie Rock", "Indie Rock"),
        ("Bachata", "Bachata"),
        ("Techno", "Techno"),
        ("House", "House"),
        ("Grunge", "Grunge"),
        ("Hard Rock", "Hard Rock"),
        ("Emo", "Emo"),
        ("Black Metal", "Black Metal"),
        ("R&B", "R&B"),
        ("Glam Metal", "Glam Metal"),
        ("Death Metal", "Death Metal"),
        ("other", "other"),
        ("Dubstep", "Dubstep"),
        ("Gothic", "Gothic"),
        ("Folk metal", "Folk metal"),
        ("Heavy metal", "Heavy metal")
    )
    genre = models.CharField(
                            max_length=100,
                            choices=sorted(GENRE_CHOICES,
                            key=lambda x:x[1]),
                            default="Alternative Rock"
                            )
    track_list = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CONDITION_CHOICES = (
        ("New", "New"),
        ("Good", "Good"),
        ("Used", "Used"),
    )
    condition = models.CharField(
                            max_length=9,
                            choices=sorted(CONDITION_CHOICES,
                            key=lambda x:x[1]),
                            default="Good"
                            )
    image = models.ImageField(
        upload_to='images/', default='../default_record_ibxfab'
    )

    released =  models.IntegerField(null=True, blank=True, default=0)
    price =  models.CharField(max_length=9, default="100 sek")
    location = models.CharField(max_length=50, default="Stockholm")
    contact = models.CharField(max_length=50, default="email: example@email.com")
    class Meta:
        ordering = ["-created"]
    
    class Meta:
        managed = True
        db_table = 'records_record'

    def __str__(self):
        return f"{self.title}"