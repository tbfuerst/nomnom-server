from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.


class Tag_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def ___str___(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Tag_Category, on_delete=models.CASCADE)

    def ___str___(self):
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def ___str___(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="creator")
    name = models.CharField(max_length=64)
    image = models.TextField()
    image_thumbnail = models.TextField()
    amount_persons = models.PositiveSmallIntegerField()
    cook_time_minutes = models.PositiveSmallIntegerField()
    instructions = models.CharField(max_length=4096)
    is_deleted = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    subscribed_by = models.ManyToManyField(
        'auth.User',  related_name="subscribers", blank=True)

    def ___str___(self):
        return self.name


class IngredientSet(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(
        Recipe, related_name='ingredientsets', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredient, related_name='ingredientName', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=32, default='')

    def ___str___(self):
        return self.name


class Recipe_Book(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    recipe = models.ManyToManyField(Recipe)

    def ___str___(self):
        return self.id
