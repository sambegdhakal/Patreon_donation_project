from django.urls import path
from . import views

app_name = "page"
urlpatterns = [
    path("createpage/", views.patreon_page_create, name= "createpage"), 
    path("viewpage/", views.patreon_page_list, name= "patreon_page_list"),
    path("deletepage/<int:id>/", views.patreon_page_delete, name= "patreon_page_delete"),
    path("updatepage/<int:id>/", views.patreon_page_update, name= "patreon_page_update"),
    path("pagedonation/<int:id>/", views.patreon_page_donation, name= "patreon_page_donation"),
]