from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path(r'',views.home,name='home'),
    path(r'images/', views.image_upload,name='upload'),
    path(r'profile/', views.profile_info,name='profile'),
    path(r'edit/', views.profile_edit,name='edit'),
    path(r'new_comment/(\d+)/', views.add_commment,name='newComment'),
    path(r'comment/', views.comments,name='comments'),
    path(r'likes/(\d+)/', views.like_images,name='likes'),
    path(r'user/',views.search_user,name='search_user')
]