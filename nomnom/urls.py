from django.urls import include, path
from rest_framework import routers
from . import api


urlpatterns = [
    path('get-all-tag-categories', api.get_all_tag_categories),
]
