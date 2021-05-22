from django.shortcuts import render, get_object_or_404, redirect
from .models import Songs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST


def home(request):
    context = {
        'songs': Songs.objects.all()
    }
    return render(request, 'home.html', context)


class SongListView(ListView):
    model = Songs
    template_name = 'home.html'
    context_object_name = 'songs'
    paginate_by = 2


class SongDetailView(DetailView):
	model = Songs
	template_name = 'song_detail.html'

class AuthorSongListView(ListView):
    model = Songs
    template_name = 'author_songs.html'
    context_object_name = 'songs'
    paginate_by = 2

    def get_queryset(self):
   		return Songs.objects.filter(author=self.kwargs.get('author'))



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})



def search(request):
    try:
        q = request.GET.get('search')
    except:
        q = None
    if q:
        song = Songs.objects.filter(title__icontains=q)
        context = {'query': q, 'song': song}
        template = 'results.html'
        print(q)
    else:
        template = 'home.html'
        context = {}
    return render(request, template, context)




@login_required
@require_POST
def add_to_fav_songs(request, id):
    fav_song = get_object_or_404(Songs, id=id)
    fav_song.favorited_by.add(request.user)
    messages.success(request, 'Added to favourite songs')
    return redirect('/')

class Fav_songs(LoginRequiredMixin, ListView):
    model = Songs
    template_name = 'fav_songs.html'
    context_object_name = 'fav_song'
    paginate_by = 2

    def get_queryset(self):
        return Songs.objects.filter(favorited_by=self.request.user)


def Profile(request, user):
    model = Songs
    user = request.user
    songs = Songs.objects.filter(favorited_by=user)
    context = {'songs': songs}
    return render(request, 'profile.html',  context)


def about(request):
    return render(request, 'about.html')