from django.contrib import admin

from .models import Tag_Category, Tag, Recipe


# Register your models here.
admin.site.register(Tag_Category)
admin.site.register(Tag)
admin.site.register(Recipe)
