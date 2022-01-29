from django.db import models
from django.core.validators import MinLengthValidator
import re
from PIL import Image

class Video(models.Model):
    title = models.CharField("Tytuł", max_length=50)
    description = models.TextField("Opis",
                    validators=[MinLengthValidator(50)])
    thumbnail = models.ImageField("Miniaturka", upload_to="video_thumbnails")
    url = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.thumbnail:
            # resizes photo
            thumb = Image.open(self.thumbnail.path)
            thumb.thumbnail((854, 480), Image.ANTIALIAS)
            thumb.save(self.thumbnail.path)

    def iframe(self):
        try: # gets id of youtube video from url which is then used to embed the video
            id = re.split("watch\?v=|be/|&", str(self.url))[1]
        except: #if there is an error it appends 0 which is ignored in template
            id = 0
        return id
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'

class Photo(models.Model):
    photo = models.ImageField("Zdjęcie", upload_to="photos")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo: 
            # resizes photo
            pic = Image.open(self.photo.path)
            pic.thumbnail((854, 480), Image.ANTIALIAS)
            pic.save(self.photo.path)
    
    def __str__(self):
        return re.split("photos/", str(self.photo))[1]

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"