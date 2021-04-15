from django.contrib import admin

from .models import Tag_Category, Tag, Ingredient, Recipe, IngredientSet, Recipe_Book

# Register your models here.
admin.site.register(Tag_Category)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(IngredientSet)
admin.site.register(Recipe_Book)
