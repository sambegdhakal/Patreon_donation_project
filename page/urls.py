from django.urls import path
from . import views

app_name = "page"
urlpatterns = [
    path("createpage/<int:userid>/", views.patreon_page_create, name= "createpage"), 
    path("viewpage/<int:id>/", views.patreon_page_view, name= "patreon_page_view"),
    path("deletepage/<int:id>/", views.patreon_page_delete, name= "patreon_page_delete"),
    path("updatepage/<int:id>/", views.patreon_page_update, name= "patreon_page_update"),
    path("searchpage/<str:username>/", views.patreon_page_list, name= "patreon_page_list")
]
