from django.urls import path
from . import views
from django.http import HttpResponseNotFound
from django.shortcuts import render, Http404

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('', views.home, name='home'),
    path('event/', views.event, name='event'),
    path('complains/', views.complains, name='complain'),
    path('core-team/', views.coreteam, name='coreteam'),
    path('register/', views.register, name='register'),
    path('gallery/', views.gallery, name='gallery'),
]
handler404 = custom_404_view