from rest_framework.views import APIView
from rest_framework import status
from .models import Tag_Category, Tag, Ingredient, Recipe
from .serializers import Tag_Category_Serializer, Ingredient_Serializer, Tag_Serializer, Recipe_Serializer_Short
from .api_lib.searchers import IngredientSearcher, TagSearcher
 

# Create your views here.
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
        

class Tag_Tag_Category_List(APIView):
    def get(self, request):
        tagC = Tag_Category.objects.all()
        tags = Tag.objects.all()
        tagC_serializer = Tag_Category_Serializer(tagC, many=True)
        tags_serializer = Tag_Serializer(tags, many=True)

        tagInformation = {'tags': tags_serializer.data, 'tagCategories': tagC_serializer.data}
        
        return JsonResponse(tagInformation, status=status.HTTP_200_OK)

        
        
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


class Tag_Category_List(APIView):
    def get(self, request, format=None):
        tag_categories = Tag_Category.objects.all()
        serializer = Tag_Category_Serializer(tag_categories, many=True)
        return JsonResponse(serializer.data)
