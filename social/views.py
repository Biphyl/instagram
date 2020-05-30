from django.shortcuts import render, redirect
from .forms import ImageProfileForm,ImageUploadForm,CommentForm
from .models import Image, Comments, Profile

# Create your views here.


def home(request):
    images = Image.objects.all()

    return render(request, 'index.html',{"images":images})
    
