from django.conf.urls.static import static
from django.urls import path
from itmusic import views
from untitled3 import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in_page, name='sign_in'),
    path('sign_up', views.sign_up_page, name='sign_up'),
    path('register_user', views.register_user, name='register'),
    path('login_user', views.login_user, name='login'),
    path('sign_out', views.sign_out, name='logout'),
    path('search', views.search_page, name='search'),
    path('find', views.SearchMusic.as_view(), name='find'),
    path('profile', views.get_view, name='profile'),
    path('music/<int:id>/', views.get_music, name='music'),
    path('add_to_playlist', views.add_to_playlist, name='add_to_playlist'),
    path('remove_from_playlist', views.remove_from_playlist, name='remove_from_playlist'),
    path('contacts', views.get_contact_page, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
