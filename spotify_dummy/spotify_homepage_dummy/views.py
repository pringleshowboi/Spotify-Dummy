from django.shortcuts import render
from .models import Playlist
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    playlist = Playlist.objects.all()
    return render(request, "homepage.html", {'playlist': playlist})

@login_required
def songs(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = playlist.songs_set.all()
    return render(request, 'songs.html', {'playlist': playlist, 'songs': songs})
