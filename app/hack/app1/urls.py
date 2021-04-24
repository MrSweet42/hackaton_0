from django.urls import path

from .views import *

urlpatterns = [
    path('', hello, name='hello'),
    path('table/', table, name='table'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail')
]
