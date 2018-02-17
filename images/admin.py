from django.contrib import admin
from .models import Image


# Register the Admin classes for Image using the decorator
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']