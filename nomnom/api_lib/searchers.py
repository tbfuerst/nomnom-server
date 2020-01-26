from ..models import Ingredient, IngredientSet, Recipe
from collections import Counter 

class TagSearcher:
    def __init__(self, search_content: list):
        self.searched_tags = search_content
    
    def search(self):
        return "searching tags...."

class IngredientSearcher:
    def __init__(self, search_content: list, search_type: str):
        self.searched_ingredients = search_content
        self.operator = search_type

    def or_search(self):
        intro = "Searching: \"" + \
            ', '.join(self.searched_ingredients) + \
            "\" with operator: " + self.operator
        print(intro)

        # The following code creates a List ingredient_sets_queries which contains all ingredient_sets
        # containing the searched Ingredients
        ingredient_sets = []
        for ingredient_word in self.searched_ingredients:
            found_ingredient_set = IngredientSet.objects.filter(
                ingredient__name=ingredient_word)  # field lookup
            ingredient_sets += found_ingredient_set

        # extract and save the found recipes
        found_recipes = []
        for ingredient_set in ingredient_sets:
            found_recipes.append(ingredient_set.recipe)

        # reduce list to unique Recipes
        countedRecipes = Counter(found_recipes)
        uniqueRecipeList = []
        for uniqueRecipe in countedRecipes:
            uniqueRecipeList.append(uniqueRecipe)

        return uniqueRecipeList

    def and_search(self):
        intro = "Searching: \"" + \
            ', '.join(self.searched_ingredients) + \
            "\" with operator: " + self.operator
        print(intro)

        search_word_count = len(self.searched_ingredients)

        # This code creates a List ingredient_sets_queries which contains all ingredient_sets
        # containing the searched Ingredients

        ingredient_sets_queries = []
        for ingredient_word in self.searched_ingredients:
            found_ingredient_set = IngredientSet.objects.filter(
                ingredient__name=ingredient_word)  # field lookup
            ingredient_sets_queries.append(found_ingredient_set)

        ##
        # The following code creates a List recipe_list, which contains all Recipes 
        # associated with the found ingredient_sets. 
        # This means, the found recipes contain the searched Ingredients

        recipe_list = []

        #search every search query separately
        for ingredient_sets_query in ingredient_sets_queries:
            current_query = []
            # get the assigned recipe to the current ingredient_set
            for ingredient_set in ingredient_sets_query:
                current_query.append(ingredient_set.recipe)

            ## one recipe could theoretically contain multiple found ingredient sets
            ## the following code block reduces the found recipes to unique values
            counted_query_recipes = Counter(current_query)
            unique_recipe_list = []
            for unique_recipe in counted_query_recipes:
                unique_recipe_list.append(unique_recipe)

            # add the unique recipes to recipe_list
            recipe_list += (unique_recipe_list)

        
        # now that all recipes are added, all recipes are extracted, which appear
        # n times in the List
        # where n is the search_word_count
        c = Counter(recipe_list)
        search_word_equals = Counter(recipe for recipe in c.elements() if c[recipe] == search_word_count)
        
        # make a list out of it
        found_recipes = []
        for found_recipe in search_word_equals:
            found_recipes.append(found_recipe)

        return found_recipes
