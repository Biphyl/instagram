from django import forms
from .models import Image,Profile,Comments

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','user','likes','comments']

class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','date_posted']