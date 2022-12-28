from django.shortcuts import render

# Create your views here.

def Next_in_line(request):
    return render(request, 'next_in_line.html')