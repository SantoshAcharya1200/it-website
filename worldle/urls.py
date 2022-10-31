from django.urls import path

from . import views

urlpatterns = [
    path('', views.worldle, name='index'),
    path('worldle', views.worldle, name='index'),


]