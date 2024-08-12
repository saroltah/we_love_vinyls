from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Record(models.Model):
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    GENRE_CHOICES = (
        ("pop", "Pop"),
        ("rock", "Rock"),
        ("blues", "Blues"),
        ("country", "Country"),
        ("electronic", "Electronic"),
        ("punk", "Punk"),
        ("classical", "Classical"),
        ("alternative-rock", "Alternative Rock"),
        ("progressive-rock", "Progressive Rock"),
        ("folk-music", "Folk music"),
        ("synth-pop", "Synth-pop"),
        ("hip-hop", "Hip-hop"),
        ("jazz", "Jazz"),
        ("funk", "Funk"),
        ("reggae", "Reggae"),
        ("disco", "Disco"),
        ("soul", "Soul"),
        ("dance", "Dance"),
        ("ska", "Ska"),
        ("indie-rock", "Indie Rock"),
        ("bachata", "Bachata"),
        ("techno", "Techno"),
        ("house", "House"),
        ("grunge", "Grunge"),
        ("hard-rock", "Hard Rock"),
        ("emo", "Emo"),
        ("black-metal", "Black Metal"),
        ("r-and-b", "R&B"),
        ("glam-metal", "Glam Metal"),
        ("death-metal", "Death Metal"),
        ("other", "other"),
        ("dubstep", "Dubstep"),
        ("gothic", "Gothic"),
        ("folk-metal", "Folk metal"),
        ("heavy-metal", "Heavy metal")
    )
    genre = models.CharField(
                            max_length=100,
                            choices=sorted(GENRE_CHOICES,
                                           key=lambda x: x[1]),
                            default="alternative-rock"
                            )
    tracklist = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CONDITION_CHOICES = (
        ("new", "New"),
        ("good", "Good"),
        ("used", "Used"),
    )
    condition = models.CharField(
                            max_length=9,
                            choices=sorted(CONDITION_CHOICES,
                                           key=lambda x: x[1]),
                            default="good"
                            )
    image = models.ImageField(
        upload_to='images/', default='../default_record_ibxfab'
        )
    released = models.IntegerField(null=True, default=0)
    price = models.CharField(max_length=9, default="100 sek")
    location = models.CharField(max_length=50, default="Stockholm")
    contact = models.CharField(max_length=50,
                               default="email: example@email.com")

    class Meta:
        ordering = ["-created"]

    class Meta:
        managed = True
        db_table = 'records_record'

    def __str__(self):
        return f"{self.title}"
