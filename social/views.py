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

def profile_info(request):
    current_user = request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts = request.user.image_set.all()

    return render(request,'profile.html',{"images":posts, "profile":profile_info,"current_user":current_user})

def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ImageProfileForm()
        return render(request,'edit_profile.html',{"form":form})