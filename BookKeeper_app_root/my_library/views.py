from django.shortcuts import render, get_object_or_404
from .models import  Book, Author, Status, Language
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from my_library.forms import RenewBookForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
# create a search bar
def Bookshelf(request):
    books = Book.objects.all()
    # book_instance = BookInstance.objects.all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    all_books=paginator.get_page(page)


    # Render the HTML template index.html with the data in the context variable.
    context={
        'books': all_books,
    }
    return render(request,'bookshelf.html', context)
       

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name']
    permission_required = 'my_library.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    permission_required = 'my_library.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'my_library.can_mark_returned'


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'pg_num', 'language', 'status']
    permission_required = 'my_library.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'pg_num', 'language', 'status']
    permission_required = 'my_library.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'my_library.can_mark_returned'





# # Create your views here.
# def index(request):
#     listings = Listing.objects.order_by('-list_date').filter(is_published=True)
#     paginator = Paginator(listings, 3)
#     page = request.GET.get('page')
#     paged_listings = paginator.get_page(page)
    
#     context = {
#         'listings': paged_listings,
#     }
#     return render(request, 'listings/listings.html', context)

# def listing(request, listing_id):
    
    
#     listing = get_object_or_404(Listing, pk=listing_id)
    
#     context = {
#         'listing' : listing
#     }
#     return render(request, 'listings/listing.html', context)

# def search(request):
#     queryset_list = Listing.objects.order_by('-list_date')

#   # Keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_list = queryset_list.filter(description__icontains=keywords)

#   # City
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city:
#             queryset_list = queryset_list.filter(city__iexact=city)

#   # State
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state:
#             queryset_list = queryset_list.filter(state__iexact=state)

#   # Bedrooms
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

#   # Price
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_list = queryset_list.filter(price__lte=price)

#     context = {
        
#     'state_choices': state_choices,
#     'bedroom_choices': bedroom_choices,
#     'price_choices': price_choices,
#     'listings': queryset_list,
#     'values': request.GET,
#   }

#     return render(request, 'listings/search.html', context)


