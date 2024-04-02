from django.contrib import admin
from .models import Dog

class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "race", "birth_date")

admin.site.register(Dog, DogAdmin)