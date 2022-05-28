from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Song, Artists,Playlist


class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',  'password1', 'password2')


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'songs']
    title = forms.TextInput()
    user = User
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

# class PlaylistForm(forms.ModelForm):
#     class Meta:
#         model = Playlist
#         fields = ['title', 'songs']
#     title = forms.TextField()
#     songs = forms.ModelMultipleChoiceField(
#         queryset=Song.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )