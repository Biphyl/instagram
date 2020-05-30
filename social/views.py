from django.shortcuts import render
from .models import Image

# Create your views here.


def home(request):
    images = Image.objects.all()

    return render(request, 'index.html',{"images":images})
    
