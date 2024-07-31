from django.urls import path
from .views import fetch_images, image_detail

urlpatterns = [
    path('', fetch_images, name='home'),
    path('image/<int:pk>/', image_detail, name='image-detail'),
]
