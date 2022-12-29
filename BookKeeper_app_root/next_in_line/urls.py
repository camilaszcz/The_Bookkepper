from django.urls import path
from . import views


urlpatterns = [
    path('next_in_line/', views.Next_in_line, name='next_in_line'),
]