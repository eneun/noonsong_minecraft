#앱 내의 urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.result, name='result'),
    path('reservation', views.reservation, name='reservation'),
    path('change/', views.change, name='change'),
    path('fever/', views.fever, name='fever'),
    path('completion/<int:id>/', views.completion, name='completion'),
    path('delete/', views.delete, name="delete"),
]