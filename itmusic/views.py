import os
from itertools import chain

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from mutagen.mp3 import MP3

from itmusic.models import Profile, Music, Playlist, Genre, PlaylistItem


class SearchMusic(ListView):
    template_name = 'search_page.html'
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            music_result = Music.objects.search(query)
            queryset_chain = chain(
                music_result
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)
            return qs
        return Music.objects.none()


def index(request):
    genre = Genre.objects.all()
    music = Music.objects.all()
    context = {
        'genres': genre,
        'musics': music
    }
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        playlist = Playlist.objects.get(user=profile)
        playlist_item = PlaylistItem.objects.filter(playlist=playlist)
        playlist_musics = []
        for p in playlist_item:
            playlist_musics.append(p.music)
        context['playlist_musics'] = playlist_musics
    return render(request, "base.html", context)


def sign_in_page(request):
    return render(request, "sign_in.html")


def sign_up_page(request):
    return render(request, 'sign_up.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        image = request.POST['image']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name,
                                            password=password)
            user.save()
            profile = Profile.objects.create(user=user, image=image)
            profile.save()
            playlist = Playlist.objects.create(user=profile)
            playlist.save()
            return redirect('sign_in')
        else:
            return render(request, 'sign_up.html', {'error': True})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'sign_in.html', {'error': True})


@login_required
def sign_out(request):
    logout(request)
    return redirect('index')


def search_page(request):
    return render(request, 'search_page.html')


def get_view(request):
    profile = Profile.objects.get(user=request.user)
    playlist = Playlist.objects.get(user=profile)
    context = {'profile': profile,
               'playlist': playlist}
    return render(request, 'profile.html', context)


@login_required()
def add_to_playlist(request):
    if request.is_ajax():
        music = Music.objects.get(id=request.GET['id'])
        profile = Profile.objects.get(user=request.user)
        playlist = Playlist.objects.get(user=profile)
        for p in playlist.playlistitem_set.all():
            if p.music == music:
                return redirect('index')
        playlist_item = PlaylistItem.objects.create(music=music, playlist=playlist)
        playlist_item.save()
        return JsonResponse({'success': str(1)}, safe=False)


def remove_from_playlist(request):
    if request.is_ajax():
        profile = Profile.objects.get(user=request.user)
        playlist = Playlist.objects.get(user=profile)
        PlaylistItem.objects.get(id=request.GET['playlist_item']).delete()
        return JsonResponse({'count': str(playlist.playlistitem_set.count())}, safe=False)


def get_music(request, id):
    music = Music.objects.get(id=id)
    audio = MP3(music.file.path)
    minute = int(audio.info.length//60)
    second = str(int(audio.info.length - (minute * 60)))
    duration = str(minute) + ":" + second
    context = {
        'music': music,
        'duration': duration
    }
    return render(request, 'music.html', context)


def get_contact_page(request):
    return render(request, 'contact.html')
