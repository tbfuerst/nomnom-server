from django.urls import include, path
from rest_framework import routers
from . import api


urlpatterns = [
    path('get-all-tag-categories', api.get_all_tag_categories),
    path('get-all-tags', api.get_all_tags),
    path('get-all-ingredients', api.IngredientsList.as_view()),
    path('search-by-ingredient', api.IngredientsSearch.as_view()),
]
