from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "player"

urlpatterns = [
    # path('songs/<str:name>/', views.IndexView.as_view(),name='index'),
    path("songs/<str:name>/", views.index, name='index'),
    path("", views.artists, name='artists'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('album/add',views.AlbumCreate.as_view(),name='album-add'),
    path("playlists/<str:title>", views.playlists, name='playlists'),
    path("createplaylist/", views.createPlaylist, name='creat_playlist'),
]
urlpatterns += staticfiles_urlpatterns()