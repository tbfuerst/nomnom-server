from django.core.management.base import BaseCommand, CommandError

from nomnom.models import Tag_Category, Tag, Ingredient, Recipe, IngredientSet, Recipe_Book

from django.contrib.auth.models import User

from random_words import RandomWords
from datetime import date
import random as rnd

# dirty seeder


class Command(BaseCommand):
    help = 'Creates mock data and fills database with it.'

    def handle(self, *args, **options):
        amount_tag_categories = 5
        amount_tags = 30
        amount_ingredients = 10
        amount_recipes = 10
        amount_ingred_sets = 100

        def rword(count, separator):
            rand = RandomWords()
            r = rand.random_words(count=count)
            words = separator.join(r)
            return words

        def rfloat():
            return (rnd.random()*1000).__round__(2)

        def rint():
            return int((rnd.random()*2000).__round__(0))

        def get_rnd_date(year):
            start_dt = date.today().replace(day=1, month=1).toordinal()
            end_dt = date.today().replace(day=31, month=12).toordinal()
            random_days = rnd.randint(start_dt, end_dt)
            if (random_days == 737484): # handle Feb 29
                random_days = 737483
            rnd_date = date.fromordinal(random_days)
            rnd_date.replace(year=year)
            return rnd_date

        def get_rnd_recipe():
            recipes = Recipe.objects.all()
            return recipes[rnd.randint(0, amount_recipes-1)]

        def rints(count, separator):
            numbers = []
            for _ in range(count):
                rng = int(rnd.random()*32000)
                strrng = str(rng)
                numbers.append(strrng)
            concat_numbers = separator.join(numbers)
            return concat_numbers
        
        def rnumber(lower, upper):
            return rnd.randint(lower,upper) 

        def get_rnd_user():
            users = User.objects.all()
            user = users[rnumber(1,2)]
            return user
            
        def tag_categories():
            Tag_Category.objects.all().delete()
            for _ in range(amount_tag_categories):
                tagC = Tag_Category(name=rword(1,""))
                tagC.save()
            
        def tags():
            Tag.objects.all().delete()
            tagCs = Tag_Category.objects.all()

            def get_random_tag_cat():
                tagCat = tagCs[int((rnd.random()*(amount_tag_categories-1)).__round__(0))]
                return tagCat

            for _ in range(amount_tags):
                tagC = get_random_tag_cat()
                tag = Tag(name=rword(1,""), category=tagC)
                tag.save()
        
        def ingredients():
            Ingredient.objects.all().delete()

            for _ in range(amount_ingredients):
                ingred = Ingredient(name=rword(1,""))
                ingred.save()
        
        def recipes():
            Recipe.objects.all().delete()
            tags = Tag.objects.all()

            def get_rnd_tags():
                tag = tags[int((rnd.random()*(amount_tags-1)).__round__(0))]
                return tag

            for _ in range(amount_recipes):

                recipe = Recipe(creator=get_rnd_user(), name=rword(3," "), amount_persons = randint(1,12),cook_time_minutes=randint(10,180), instructions=rword(140," "),is_deleted=False)
                recipe.save()

            print("assigning recipe tags...")
            all_recipes = Recipe.objects.all()
            def assign_rnd_tags():
                for i in range(amount_recipes):
                    recipe = all_recipes[i]
                    rnd_tag_amount = randint(1,4)
                    for _ in range(rnd_tag_amount):
                        tag = get_rnd_tags()
                        recipe.tags.add(tag)
                    recipe.save()
            assign_rnd_tags()
            print("tags assigned!")

        def ingredientsets():
            IngredientSet.objects.all().delete()

            def get_rand_ingred():
                ingredients = Ingredient.objects.all()
                return ingredients[randint(0, (amount_ingredients-1))]
                
            for _ in range(amount_ingred_sets):
                ingredientset = IngredientSet(recipe=get_rnd_recipe(), ingredient=get_rand_ingred(), amount=randint(1,4000), unit=rword(1,""))
                ingredientset.save()

        def recipeBooks():
            Recipe_Book.objects.all().delete()
            users = User.objects.all()

            for i in range(1,3):
                rb = Recipe_Book(user=users[i])
                rb.save()
            
            print("assigning recipes to recipeBook...")
            all_recipe_books = Recipe_Book.objects.all()
            def assign_rnd_recipes():
                for i in range(2):
                    rb = all_recipe_books[i]
                    rnd_recipe_amount = randint(1, int((amount_recipes-1)/2))
                    for j in range(rnd_recipe_amount):
                        recipe = get_rnd_recipe()
                        rb.recipe.add(recipe)
                    recipe.save()
            assign_rnd_recipes()
            print("recipes assigned")

        print("Seeding Tag Categories")
        tag_categories()
        print("Seeding Tags")
        tags()
        print("Seeding Ingredients")
        ingredients()
        print("Seeding Recipes")
        recipes()
        print("Seeding IngredientSets")
        ingredientsets()
        print("Seeding Recipe Books")
        recipeBooks()
        print("Seeding successful")
