#앱 내의 urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('clearfeed/', views.clearfeed, name='clearfeed'),
    path('createcomment/<int:id>', views.createcomment, name='createcomment'),
]