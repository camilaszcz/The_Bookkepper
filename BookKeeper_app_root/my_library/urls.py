from django.urls import path
from . import views

urlpatterns = [
    path('booklist/', views.booklist, name='booklist'),
    path('booklist/book_add/', views.book_add, name='book_add'),
    path('booklist/<int:id>/', views.bookdetail, name='book_detail'),
]



