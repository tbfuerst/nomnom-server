from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'webapp.html')


def fontmanifest(request):
    return HttpResponseRedirect('/nomnom/static/assets/FontManifest.json')


def assetmanifest(request):
    return HttpResponseRedirect('/nomnom/static/assets/AssetManifest.json')


def materialicons(request):
    return HttpResponseRedirect('/nomnom/static/assets/fonts/MaterialIcons-Regular.ttf')


def cupertinoicons(request):
    return HttpResponseRedirect('/nomnom/static/assets/packages/cupertino_icons/assets/CupertinoIcons.ttf')


def logo(request):
    return HttpResponseRedirect('/nomnom/static/assets/resources/images/nomnomlogo_book_only.png')
