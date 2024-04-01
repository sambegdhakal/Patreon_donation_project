# donation_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Import HttpResponse

# Dummy view function
def dummy_view(request):
    return HttpResponse("This is a dummy view.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('dummy/', dummy_view),  # Add a dummy URL pattern
]

# Print urlpatterns for debugging
print("URL patterns:", urlpatterns)
