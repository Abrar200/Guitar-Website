from django.contrib import admin
from django.urls import path
from songs import views
from songs.views import Fav_songs
from songs.views import SongListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SongListView.as_view(), name='home'),
    path('author/<str:author>', views.AuthorSongListView.as_view(), name='author-songs'),
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('s/', views.search, name='search'),
    path('add-to-fav-songs/<int:id>/', views.add_to_fav_songs, name='add-to-fav-songs'),
    path('favourite-songs/', Fav_songs.as_view(), name='favourite-songs'),
    path('profile/<str:user>', views.Profile, name='profile'),
    path('about/', views.about, name='about'),
]
