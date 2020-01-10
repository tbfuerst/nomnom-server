from rest_framework import serializers

from .models import Tag_Category

class Tag_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag_Category
        fields = ['id', 'name']
 

# doku: https://www.django-rest-framework.org/tutorial/1-serialization/#working-with-serializers
