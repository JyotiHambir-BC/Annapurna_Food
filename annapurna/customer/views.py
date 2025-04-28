from django.shortcuts import render
from django.views import View
from .models import RecipeItem, Category

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')
    
class Recipe(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        appetizers = RecipeItem.object.filter(categoty__name__contains = 'Appetizer')
        rice_dishes = RecipeItem.object.filter(categoty__name__contains = 'Rice Dishes')
        chuttney = RecipeItem.object.filter(categoty__name__contains = 'Chuttney')
        drinks = RecipeItem.object.filter(categoty__name__contains = 'Drinks')
        curry = RecipeItem.object.filter(categoty__name__contains = 'Curry')
        dessert = RecipeItem.object.filter(categoty__name__contains = 'Dessert')
        snacks = RecipeItem.object.filter(categoty__name__contains = 'Snacks')
        
        # pass into context
        context = {
            'appetizers': appetizers,
            'rice_dishes': rice_dishes,
            'chuttney': chuttney,
            'drinks': drinks,
            'curry': curry,
            'dessert': dessert,
            'snacks': snacks,
        }

        # render the template
        return render(request, 'customer/recipe.html')