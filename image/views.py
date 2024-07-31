from django.shortcuts import render, get_object_or_404
import requests
from .models import Image
from django.conf import settings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv('PIXABAY_API_KEY')
API_URL = f"https://pixabay.com/api/?key={API_KEY}&per_page=200&q=food"

def fetch_images(request):
    if not Image.objects.exists():
        response = requests.get(API_URL)
        data = response.json()

        for item in data['hits']:
            Image.objects.create(
                pixabay_id=item['id'],
                page_url=item['pageURL'],
                type=item['type'],
                tags=item['tags'],
                preview_url=item['previewURL'],
                webformat_url=item['webformatURL'],
                large_image_url=item['largeImageURL'],
                image_width=item['imageWidth'],
                image_height=item['imageHeight'],
                views=item['views'],
                downloads=item['downloads'],
                likes=item['likes'],
                comments=item['comments'],
                user=item['user'],
                user_image_url=item['userImageURL'],
            )
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'detail.html', {'image': image})
