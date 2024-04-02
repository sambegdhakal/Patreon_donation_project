from django.urls import path
from . import views

app_name = "page"
urlpatterns = [
    path("createpage/", views.patreon_page_create, name= "createpage"), 
    path("viewpage/", views.patreon_page_list, name= "patreon_page_list"),
]