# Generated by Django 3.2.6 on 2021-09-05 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Zdjęcie')),
            ],
            options={
                'verbose_name': 'Zdjęcie',
                'verbose_name_plural': 'Zdjęcia',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tytuł')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(50)], verbose_name='Opis')),
                ('thumbnail', models.ImageField(upload_to='video_thumbnails', verbose_name='Miniaturka')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmy',
            },
        ),
    ]
