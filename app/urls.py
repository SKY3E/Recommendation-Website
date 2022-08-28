from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('uploadform', views.uploadform, name='uploadform'),
]