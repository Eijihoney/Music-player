from django.contrib import admin
from . models import Song, Artists, Playlist

# Register your models here.
admin.site.register(Song)
admin.site.register(Artists)
admin.site.register(Playlist)