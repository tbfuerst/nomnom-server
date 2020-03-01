from django.urls import path
from rest_framework.authtoken import views
from . import api


urlpatterns = [
    path('api-login', views.obtain_auth_token),
    path('get-all-ingredients', api.Ingredients_List.as_view()),
    path('search-by-ingredient', api.Ingredients_Search.as_view()),
    path('search-by-tag', api.Tag_Search.as_view()),
    path('search-for-recipe', api.Recipe_Search.as_view()),
    path('recipe-details', api.Recipe_Details.as_view()),
    path('get-full-tag-info', api.Tag_Tag_Category_List.as_view()),
    path('get-recipe-list', api.Recipe_List.as_view()),
]
