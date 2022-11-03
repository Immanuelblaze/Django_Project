from email import contentmanager
from turtle import title
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    
class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField('date released')
    likes = models.IntegerField(default=0)
    artise_id = models.CharField(max_length=50)
    

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    song_id = models.CharField(max_length=50)
    
    