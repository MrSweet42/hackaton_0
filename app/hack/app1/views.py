from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Tag


def hello(request):
    n = 'Константин'
    return render(request, 'app1/main.html', context={'name': n})


def table(request):
    posts = Post.objects.all()
    return render(request, 'app1/table.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'app1/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'app1/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'app1/tag_detail.html', context={'tag': tag})
