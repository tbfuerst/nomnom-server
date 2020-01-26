from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .models import Tag_Category, Tag, Ingredient
from .serializers import Tag_Category_Serializer, Ingredient_Serializer, Tag_Serializer, Recipe_Serializer
import json
from .api_lib.searchers import IngredientSearcher
 

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


class IngredientsList(APIView):
    """
    List all ingredients or search by ingredients
    """

    def get(self, request, format=None):
        ingredients = Ingredient.objects.all()
        serializer = Ingredient_Serializer(ingredients, many=True)
        return JsonResponse(serializer.data, safe=False)

class IngredientsSearch(APIView):
    def post(self, request, format=None):
        try:
            searcher = IngredientSearcher(request.data[1:], request.data[0])
            if (request.data[0] == "AND"):
                recipes = searcher.and_search()
            else:
                recipes = searcher.or_search()
            serializer = Recipe_Serializer(recipes, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception as error:
            return HttpResponse(error, status=status.HTTP_400_BAD_REQUEST)
        
        
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def get_all_tag_categories(request):
    if request.method == 'GET':
        tagC = Tag_Category.objects.all()
        serializer = Tag_Category_Serializer(tagC, many=True)
        return JsonResponse(serializer.data, safe=False)

def get_all_tags(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = Tag_Serializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)

def search_by_ingredient(request):
    if request.method == 'POST':
        return JsonResponse(["this is a post request"], safe=False)
    if request.method == 'GET':
        return JsonResponse([1, 2, 3], safe=False)

class Tag_Category_List(APIView):
    def get(self, request, format=None):
        tag_categories = Tag_Category.objects.all()
        serializer = Tag_Category_Serializer(tag_categories, many=True)
        return Response(serializer.data)
