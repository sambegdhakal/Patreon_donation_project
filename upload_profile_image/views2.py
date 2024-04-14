from django.shortcuts import render
from .models import Image

def get_images_by_user(request, user_id):
    images = Image.objects.filter(user_id=user_id)
    #image_urls = [image.image_url for image in images]
    image_urls = [f"C:/Users/Sambeg/OneDrive/Desktop/Image_upload_test/image_upload_project/images{image.image_url}" for image in images]
    return render(request, 'image_gallery.html', {'image_urls': image_urls})
