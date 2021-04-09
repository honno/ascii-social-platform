from django.urls import path

from .views import *


app_name = "core"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("join", JoinView.as_view(), name="join"),
    path("sign_in", SignInView.as_view(), name="sign_in"),
    path("sign_out", SignOutView.as_view(), name="sign_out"),
    path("users/", UserListView.as_view(), name="users"),
    path("users/<slug:username>", UserView.as_view(), name="user"),
    path("add", AddArtView.as_view(), name="add"),
    path("art/", ArtGalleryView.as_view(), name="arts"),
    path("art/<int:pk>", ArtView.as_view(), name="art"),
    path("art/<int:pk>/edit", ArtEditView.as_view(), name="edit"),
]
