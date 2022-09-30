from enum import unique
from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["artist_name"]
    
    def __str__(self):
        return self.artist_name
   
class Album(models.Model):
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100, unique=True)
    release_date = models.DateField(blank=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to=None, default='jensen/pov/static/pov/img/default.png', height_field=None, width_field=None, max_length=100)

    class Meta:
        ordering = ["artist_name"]

    def __str__(self):
        return self.album_name