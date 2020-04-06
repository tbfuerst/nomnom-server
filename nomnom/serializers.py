from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag_Category, Tag, Recipe, Ingredient, IngredientSet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class Tag_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag_Category
        fields = ['id', 'name']


class Tag_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'category']


class Recipe_Serializer_Short(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name']


class Ingredient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class IngredientSet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientSet
        fields = ['amount', 'unit', 'ingredient']
        depth = 1  # include Ingredient Object


class Reciper(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'creator', 'name', 'amount_persons',
                  'cook_time_minutes', 'ingredientsets', 'instructions', 'tags']
        depth = 2


class Recipe_Serializer(serializers.ModelSerializer):
    ingredientsets = IngredientSet_Serializer(
        many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'creator', 'name', 'amount_persons',
                  'cook_time_minutes', 'ingredientsets', 'instructions', 'tags', 'subscribed_by']
        depth = 2

# doku: https://www.django-rest-framework.org/tutorial/1-serialization/#working-with-serializers
