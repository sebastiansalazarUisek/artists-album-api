from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    debut_date = models.DateField()
    image = models.ImageField(upload_to='artist_images/')
    
    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    number_of_tracks = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.artist.name}"