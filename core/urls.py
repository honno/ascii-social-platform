from django.urls import path

from .views import *


app_name = "core"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    path("users/", UserListView.as_view(), name="users"),
    path("users/join", JoinView.as_view(), name="join"),
    path("users/sign_in", SignInView.as_view(), name="sign_in"),
    path("users/sign_out", SignOutView.as_view(), name="sign_out"),

    path("users/<slug:username>", UserView.as_view(), name="user"),
    path("users/<slug:username>/settings", SettingsView.as_view(), name="settings"),
    path("users/<slug:username>/follow", follow_user, name="follow_user"),

    path("art/", ArtGalleryView.as_view(), name="arts"),
    path("art/post", PostArtView.as_view(), name="post_art"),

    path("art/<int:pk>", ArtView.as_view(), name="art"),
    path("art/<int:pk>/thumb.png", art_thumb, name="art_thumb"),
    path("art/<int:pk>/like", like_art, name="like_art"),
    path("art/<int:pk>/edit", ArtEditView.as_view(), name="edit_art"),

    path("nsfw_pref", nsfw_pref, name="nsfw_pref"),
]
