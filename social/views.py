from django.shortcuts import render, redirect
from .forms import ImageProfileForm,ImageUploadForm,CommentForm
from .models import Image, Comments, Profile

# Create your views here.


def home(request):
    images = Image.objects.all()

    return render(request, 'index.html',{"images":images})
    
def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ImageUploadForm()
        return render(request,'upload.html', {"form":form})

