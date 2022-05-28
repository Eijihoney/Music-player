from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from pickle import FALSE


class Artists(models.Model):
    name = models.TextField()
    surname = models.TextField()
    nickname = models.TextField()
    birthdate = models.DateTimeField()
    image = models.ImageField(default=None)

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nickname

    
class Song(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    image = models.ImageField(default=None)
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20,default='3:30')
    paginate_by = 2

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("player:detail", kwargs={"pk": self.pk})


class Playlist(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    image = models.ImageField(default=None)

    def __str__(self):
        return self.title


