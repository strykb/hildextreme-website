from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("filmy/", views.VideosView.as_view(), name="videos"),
    path("zdjecia/", views.PhotosView.as_view(), name="photos"),
    path("kontakt", views.ContactView.as_view(), name="contact")
]