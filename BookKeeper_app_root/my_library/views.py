from django.shortcuts import render, get_object_or_404
from .models import  Book, Status, Language
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from my_library.forms import CreateBookForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
# create a search bar
def Book_add(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            # create a new `Book` and save it to the db
            Book = form.save()
            # redirect to the detail page of the book we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('book_detail')

    else:
        form = CreateBookForm()

    return render(request,
                'book_add',
                {'form': form})
    
    
    # books = Book.objects.all()
    # book_instance = BookInstance.objects.all()
    # paginator = Paginator(books, 10)
    # page = request.GET.get('page')
    # all_books=paginator.get_page(page)


    # Render the HTML template index.html with the data in the context variable.
    # context={
    #     'books': all_books,
    # }
    # return render(request,'bookshelf.html', context)
       

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 5


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


# class AuthorListView(generic.ListView):
#     """Generic class-based list view for a list of authors."""
#     model = Author
#     paginate_by = 10


# class AuthorCreate(PermissionRequiredMixin, CreateView):
#     model = Author
#     fields = ['first_name', 'last_name']
#     permission_required = 'my_library.can_mark_returned'


# class AuthorUpdate(PermissionRequiredMixin, UpdateView):
#     model = Author
#     fields = '__all__' # Not recommended (potential security issue if more fields added)
#     permission_required = 'my_library.can_mark_returned'


# class AuthorDelete(PermissionRequiredMixin, DeleteView):
#     model = Author
#     success_url = reverse_lazy('authors')
#     permission_required = 'my_library.can_mark_returned'


# class BookCreate(PermissionRequiredMixin, CreateView):
#     model = Book
#     fields = ['book_cover','title', 'author', 'summary', 'pg_num', 'language', 'status']
#     permission_required = 'my_library.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['book_cover','title', 'author', 'summary', 'pg_num', 'language', 'status']
    permission_required = 'my_library.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'my_library.can_mark_returned'
