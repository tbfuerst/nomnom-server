from rest_framework.authtoken import views
from rest_framework.views import APIView
from rest_framework import status
from .models import Tag_Category, Tag, Ingredient, Recipe
from .serializers import Tag_Category_Serializer, IngredientSet_Serializer, Ingredient_Serializer, Tag_Serializer, Recipe_Serializer_Short, Recipe_Serializer
from .api_lib.searchers import IngredientSearcher, TagSearcher, RecipeSearcher, IngredientSetSearcher

# Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Response Libraries
from django.http import HttpResponse
from django.http import JsonResponse


class Ingredients_List(APIView):
    def get(self, request):
        """Returns a JSON of all Existing Ingredients"""
        ingredients = Ingredient.objects.all()
        serializer = Ingredient_Serializer(ingredients, many=True)
        return JsonResponse(serializer.data, safe=False)


class Recipe_List(APIView):
    def get(self, request):
        ''' Returns all Recipe names '''
        recipes = Recipe.objects.all()
        serializer = Recipe_Serializer_Short(recipes, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class Ingredients_Search(APIView):
    authentication_classes = (TokenAuthentication),
    permission_classes = (IsAuthenticated),

    def post(self, request):
        """Returns a JSON of Recipes which contain the ingredients,
        provided by the request

        @param: list<String> request.data
        """
        try:
            searcher = IngredientSearcher(request.data[1:], request.data[0])
            if (request.data[0] == "AND"):
                recipes = searcher.and_search()
            else:
                recipes = searcher.or_search()
            serializer = Recipe_Serializer_Short(recipes, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except RuntimeError as error:
            return HttpResponse(error, status=status.HTTP_400_BAD_REQUEST)


class Tag_Search(APIView):
    def post(self, request):
        try:
            searcher = TagSearcher(request.data)
            recipeData = searcher.search()
            return JsonResponse(recipeData, status=status.HTTP_200_OK)
        except RuntimeError as error:
            return HttpResponse(error, status=status.HTTP_400_BAD_REQUEST)


class Recipe_Search(APIView):
    def post(self, request):
        try:
            searcher = RecipeSearcher(request.data['id'])
            recipe_data = searcher.search()
            serializer = Recipe_Serializer_Short(recipe_data)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except RuntimeError as error:
            return HttpResponse(error, status=status.HTTP_400_BAD_REQUEST)


class Recipe_Details(APIView):
    def post(self, request):
        requestedID = request.data['id']
        try:
            searcher = RecipeSearcher(requestedID)
            recipe_data = searcher.search()
            recipe_serializer = Recipe_Serializer(recipe_data)
            return JsonResponse(recipe_serializer.data, status=status.HTTP_200_OK)
        except RuntimeError as error:
            return HttpResponse(error, status=status.HTTP_400_BAD_REQUEST)


class Tag_Tag_Category_List(APIView):
    def get(self, request):
        tagC = Tag_Category.objects.all()
        tags = Tag.objects.all()
        tagC_serializer = Tag_Category_Serializer(tagC, many=True)
        tags_serializer = Tag_Serializer(tags, many=True)

        tagInformation = {'tags': tags_serializer.data,
                          'tagCategories': tagC_serializer.data}

        return JsonResponse(tagInformation, status=status.HTTP_200_OK)


class Tag_Category_List(APIView):
    def get(self, request, format=None):
        tag_categories = Tag_Category.objects.all()
        serializer = Tag_Category_Serializer(tag_categories, many=True)
        return JsonResponse(serializer.data)


def index(request):
    return HttpResponse("Hello, world. You're at the index.")
