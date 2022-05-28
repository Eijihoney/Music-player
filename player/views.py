# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# imported our models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from dataclasses import fields
from pyexpat import model
from re import template
from click import edit
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Song, Artists, Playlist
from .forms import CreatUserForm, PlaylistForm

def artists(request):
    context = {"page_obj": Artists.objects.all(),
               "playlists": Playlist.objects.all()}
    return render(request, "index11.html", context)

class DetailView(generic.DetailView):
    context = {"page_obj": Artists.objects.all()}
    model=Song
    template_name ='player/detail.html'
    
    
class AlbumCreate(CreateView):
    context = {"page_obj": Artists.objects.all()}
    model=Song
    fields=['title','artist','image','audio_file']
    
# @login_required(login_url='login')
def index(request, name):
    paginator = Paginator(Song.objects.filter(artist__nickname=name), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)

# @login_required(login_url='login')
def createPlaylist(request):
    form = PlaylistForm(request.POST)
    form.user = User.objects.filter(username = request.user)[0]
    if request.method == 'POST':
        print(form.user.username)
        if form.is_valid():
            form.save()
            print("saved")
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, "createPlaylist.html", context)

# @login_required(login_url='login')
def playlists(request, title):
    songs = Playlist.objects.filter(title=title)[0]
    paginator = Paginator(songs.songs.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)


def signup(request):
    form = CreatUserForm()
    if request.user.is_authenticated:
        return redirect('player:artists')
    else:
        if request.method == 'POST':
            form = CreatUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect(reverse('player:login'))

        context = {'form': form}
        return render(request, "signup.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('player:artists')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('player:artists')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, "login.html", context)


# @login_required(login_url='login')
def artists(request):
    context = {"page_obj": Artists.objects.all(),
               "playlists": Playlist.objects.all()}
    return render(request, "index11.html", context)


def logoutUser(request):
    logout(request)
    return redirect('player:login')
