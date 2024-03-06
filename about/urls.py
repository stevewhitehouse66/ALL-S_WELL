from django.contrib import admin
from django.urls import path  # Make sure to import the 'path' function

urlpatterns = [
    # Your other URL patterns go here
    path('admin/', admin.site.urls),
]
