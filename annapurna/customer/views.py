from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import RecipeItem, Category

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')
    
# class Recipe(View):
#     def get(self, request, *args, **kwargs):
#         # get every item from each category
#         appetizers = RecipeItem.objects.filter(category__name__contains = 'Appetizer')
#         rice_dishes = RecipeItem.objects.filter(category__name__contains = 'Rice Dishes')
#         chuttney = RecipeItem.objects.filter(category__name__contains = 'Chuttney')
#         drinks = RecipeItem.objects.filter(category__name__contains = 'Drinks')
#         curry = RecipeItem.objects.filter(category__name__contains = 'Curry')
#         dessert = RecipeItem.objects.filter(category__name__contains = 'Dessert')
#         snacks = RecipeItem.objects.filter(category__name__contains = 'Snacks')
        
#         # pass into context
#         context = {
#             'appetizers': appetizers,
#             'rice_dishes': rice_dishes,
#             'chuttney': chuttney,
#             'drinks': drinks,
#             'curry': curry,
#             'dessert': dessert,
#             'snacks': snacks,
#         }

#         # render the template
#         return render(request, 'customer/recipe.html', context)
    
#     def post(self, request, *args, **kwargs):
#         return render(request, 'customer/recipe.html')
    
# class Detail_Recipe(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'customer/detail_recipe.html')

class RecipeCategoryView(View):
    def get (self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'customer/recipe_category.html', {'categories': categories})       
    
    
class RecipeListView(View):
    def get (self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        recipes = RecipeItem.objects.filter(category=category)
        return render(request, 'customer/recipe_list.html', {
            'category' : category,
            'recipes' : recipes
        })