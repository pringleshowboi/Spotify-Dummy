from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=200)
    vibe = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.name} ({self.vibe})"


class Songs(models.Model):
    playlist_name = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    artist = models.CharField(max_length=140)
    song_name = models.CharField(max_length=140)
    album = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.artist} - {self.song_name} ({self.album})"
