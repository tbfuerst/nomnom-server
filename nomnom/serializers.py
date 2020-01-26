from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Tag_Category, Tag, Recipe, Ingredient


class Tag_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag_Category
        fields = ['id', 'name']


class Tag_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'category']


class Recipe_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'creator', 'name', 'amount_persons',
                  'cook_time_minutes', 'instructions', 'tags']


class Ingredient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

# doku: https://www.django-rest-framework.org/tutorial/1-serialization/#working-with-serializers
