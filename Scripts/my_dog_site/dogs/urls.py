from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dogs/', views.dogs, name='dogs'),
    path('dogs/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing')
]

