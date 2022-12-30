from django.shortcuts import render,get_object_or_404
from .models import Book
from django.core.paginator import Paginator
from my_library.forms import CreateBookForm
from django.urls import reverse_lazy

# Create your views here.

def book_add(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            # create a new `Book` and save it to the db
            book = form.save()
            return render(request, 'my_library/book_add.html')
    else:
            form = CreateBookForm()

    return render(request,'my_library/my_library.html',{'form': form})


def booklist(request):
    book = Book.objects.order_by('-status')
    paginator = Paginator(my_library, 4)
    page = request.GET.get('page')
    paged_books = paginator.get_page(page)
    
    context = {
        'my_library': paged_books,
    }
    return render(request, 'my_library/my_library.html', context)

          
def bookdetail(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    
    context = {
        'book' : book
    }
    return render(request, 'my_library/book_detail.html', context)
