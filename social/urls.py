from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'',views.home,name='home'),
    path(r'images/', views.image_upload,name='upload'),
    path(r'profile/', views.profile_info,name='profile'),
    path(r'edit/', views.profile_edit,name='edit'),
    path(r'add_comment/(\d+)/', views.add_commment,name='add_comment'),
    path(r'comment/', views.comments,name='comments'),
    path(r'like_image/(\d+)/', views.like_images,name='like_image'),
    path(r'user/',views.search_user,name='search_user')
]