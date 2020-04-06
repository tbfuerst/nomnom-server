from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, serializers
from django.urls import path, include
from rest_framework.authtoken import views
from . import api, admin

from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()


# first we define the serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

# Create the API views


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('add-edit-recipe', api.Add_Edit_Recipe.as_view()),
    path('api-login', views.obtain_auth_token),
    path('get-all-ingredients', api.Ingredients_List.as_view()),
    path('get-full-tag-info', api.Tag_Tag_Category_List.as_view()),
    path('get-recipe-list', api.Recipe_List.as_view()),
    path('edit-subscription', api.Edit_Subscription.as_view()),
    path('recipe-details', api.Recipe_Details.as_view()),
    path('search-by-ingredient', api.Ingredients_Search.as_view()),
    path('search-by-tag', api.Tag_Search.as_view()),
    path('search-for-recipe', api.Recipe_Search.as_view()),


]
