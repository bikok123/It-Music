from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_image/", null=True)

    def __str__(self):
        return self.user.last_name + " " + self.user.first_name


class Playlist(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.pk)


class PlaylistItem(models.Model):
    music = models.ForeignKey("Music", on_delete=models.SET_NULL, null=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True)


class Artist(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='artist_image/', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    date_release = models.DateField()

    def __str__(self):
        return self.name


class MusicManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            res = (Q(name__icontains=query))
            qs = qs.filter(res).distinct()
        return qs


class Music(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country = models.CharField(max_length=25, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to="music/", null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="music_image/", null=True)
    release_date = models.DateField(null=True)
    lyrics = models.TextField(null=True)
    objects = MusicManager()

    def __str__(self):
        return self.name
