from django.shortcuts import render


from my_library.models import Book, Status, Language


# Create your views here.
def index(request):
    # books = Book.objects.all()
    # paginator = Paginator(books, 10)
    # page = request.GET.get('page')
    # all_books=paginator.get_page(page)

    # context = {
    #     "books": all_books,
    #     "status_choices": status_choices,
    #     "language_choices": language_choices,
    # }
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')

  