from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.result, name='index'),
    path('check', views.result, name='index'),
    path('about',views.about,name='about')
]