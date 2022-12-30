from django.shortcuts import render


from my_library.models import Book, Status, Language


# Create your views here.
def index(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')

  