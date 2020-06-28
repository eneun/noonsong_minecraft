#앱 내의 urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.result, name='result'),
    path('change/', views.change, name='change'),
    path('fever/', views.fever, name='fever'),

]