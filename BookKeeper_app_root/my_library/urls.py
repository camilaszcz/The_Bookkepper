from django.urls import path
from . import views

urlpatterns = [
    path('book_add', views.book_add, name='book_add'),
    path('my_library', views.booklist, name='my_library'),
    path('<int:book_id>/book', views.bookdetail, name='bookdetail'),
]