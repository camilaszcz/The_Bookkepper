from django.shortcuts import render,get_object_or_404 , redirect
from .models import Book
from django.core.paginator import Paginator
from my_library.forms import CreateBookForm
from django.urls import reverse_lazy
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your views here.

def book_add(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            # create a new `Book` and save it to the db
            book = form.save()
            # The  form.save()  method not only saves the new object to the database - it also returns that object, which means we can use it in the next step, where we immediately redirect to the newly created band. 
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('book_detail', book.id)
    else:
        form = CreateBookForm()

    return render(request,'book_add.html', {'form': form})


def booklist(request):
    books = Book.objects.all()
    return render(request,
           'booklist.html', # point to the new template name
           {'books': books})


          
def bookdetail(request, id):
    book= Book.objects.get(id=id)
    return render(request,'book_detail.html',{'book':book})

