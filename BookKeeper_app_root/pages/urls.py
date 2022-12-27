from django.urls import path
from . import views

urlpatterns = [
    path( "homepage", views.index, name='homepage'),
    path('about', views.about, name='about')
]