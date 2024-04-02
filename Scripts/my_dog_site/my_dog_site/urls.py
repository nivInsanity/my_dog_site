from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('dogs.urls')),
    path('admin/', admin.site.urls),
]