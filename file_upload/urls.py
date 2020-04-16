from django.urls import path,include
from . import views

urlpatterns = [
  	path('user/create',views.django_image_and_file_upload_ajax,name='n1')
]