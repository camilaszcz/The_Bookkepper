from django.shortcuts import render

# Create your views here.


def Current(request):
         return render(request, 'currently_reading.html')