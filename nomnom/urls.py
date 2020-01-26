from django.urls import path
from . import api


urlpatterns = [
    path('get-all-tag-categories', api.get_all_tag_categories),
    path('get-all-tags', api.get_all_tags),
    path('get-all-ingredients', api.IngredientsList.as_view()),
    path('search-by-ingredient', api.IngredientsSearch.as_view()),
    path('search-by-tag', api.TagSearch.as_view()),
    path('get-full-tag-info', api.Tag_Tag_Category_List.as_view()),
]
