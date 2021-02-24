from django.db import models
from django.urls import reverse

class Album(models.Model):
    album_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    album_logo = models.ImageField(upload_to='album/images/')
    
    def __str__(self):
        return f'{self.album_title} - {self.artist}'
    
    def get_absolute_url(self):
        return reverse('music:album-detail', kwargs={'pk': self.pk })


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.song_title