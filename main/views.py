from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Photo, Video
from .forms import ContactForm

class IndexView(ListView):
    template_name = "main/index.html"
    model = Video
    context_object_name = "videos"
    ordering = "-id"
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class VideosView(ListView):
    template_name = "main/all_videos.html"
    model = Video
    context_object_name = "videos"
    ordering = "-id"

class PhotosView(ListView):
    template_name = "main/photos.html"
    model = Photo
    context_object_name = "photos"
    ordering = "-id"

class ContactView(FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)