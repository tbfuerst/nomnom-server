from django.urls import include, path
from rest_framework import routers
from . import api


urlpatterns = [
    path('api/get-all-tag-categories', api.get_all_tag_categories),
]
