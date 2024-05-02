"""
URL configuration for Patreon_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registration.views import userregister #from views.py import userregister function; from registration app
from login.views import login #from views.py import login function; from login app
from subscription.views import patreon_page_subscription, view_page_subscription
from donation.views import patreon_page_donation, view_page_amt 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", userregister, name="register"),
    path("login/", login, name= "login"), 
    path("page/", include("page.urls")),
    path("image/", include("images.urls")),
    path("pagedonation/<int:userid>/<int:pageid>/", patreon_page_donation, name= "patreon_page_donation"),
    path("pageamt/<int:pageid>/", view_page_amt, name= "view_page_amt"),
    path("pagesubscription/<int:userid>/<int:pageid>/<str:date>/", patreon_page_subscription, name= "patreon_page_subscription"),
    path("subscriptionview/<int:pageid>/", view_page_subscription, name= "view_page_subscription"),		
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
