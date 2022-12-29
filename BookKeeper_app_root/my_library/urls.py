from django.urls import path
from . import views, forms


urlpatterns = [
    path('bookshelf/', views.BookListView.as_view(), name='bookshelf'),
    # path('book_list/', views.BookListView.as_view(), name ='books'),
    # path('booklist/', views.BookListView.as_view(), name='booklist'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    # path('authors/', views.AuthorListView.as_view(), name='authors'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book_add/', views.Book_add, name='book_add'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

# # Add URLConf to create, update, and delete authors
# urlpatterns += [
#     path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
#     path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
#     path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
# ]

