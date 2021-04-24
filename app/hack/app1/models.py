from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)  # db_index - флаг на индексацию
    slug = models.SlugField(max_length=150, unique=True)  # unique - флаг на уникальность, автоматически индексируется
    body = models.TextField(blank=True, db_index=True)  # blank=True - поле может быть пустым
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')  # связь между классами Post и Tag
    date_pub = models.DateTimeField(auto_now_add=True)  # auto_now_add=True - поле заполняется в момент сохранения в БД

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):  # чтобы выводить в консоль title
        return '{}'.format(self.title)  # в {} будут подставляться какие-то данные


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
