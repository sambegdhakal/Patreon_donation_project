from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("<int:imageid>/", views.get_image, name = "view_image"),
    path("upload/", views.upload, name = "upload_image") 
]