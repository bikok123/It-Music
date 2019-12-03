from django.contrib import admin

from itmusic.models import Profile, Genre, Music, Album, Artist, Playlist, PlaylistItem

admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(Music)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Playlist)
admin.site.register(PlaylistItem)

