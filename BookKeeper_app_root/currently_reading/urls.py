from django.urls import path
from . import views


urlpatterns = [
    path('currently_reading/', views.Current, name='currently_reading'),
]