from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .models import Tag_Category, Tag, Ingredient
from .serializers import Tag_Category_Serializer, Ingredient_Serializer, Tag_Serializer


# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


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


def get_all_ingredients(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        serializer = Ingredient_Serializer(ingredients, many=True)
        return JsonResponse(serializer.data, safe=False)


class Tag_Category_List(APIView):
    def get(self, request, format=None):
        tag_categories = Tag_Category.objects.all()
        serializer = Tag_Category_Serializer(tag_categories, many=True)
        return Response(serializer.data)
