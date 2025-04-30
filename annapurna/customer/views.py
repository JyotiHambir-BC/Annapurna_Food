from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import RecipeItem, Category

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class RecipeCategoryView(View):
    def get (self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'customer/recipe_category.html', {'categories': categories})
    
class RecipeListView(View):
    def get(self, request, category_slug):
        # Get the category based on the slug
        category = get_object_or_404(Category, slug=category_slug)

         # Filter RecipeItems based on the selected category
        recipes = RecipeItem.objects.filter(category=category)

        context = {
            'category': category,
            'recipes': recipes,
        }

        
       # Filter the RecipeItems by the category
        # appetizers = RecipeItem.objects.filter(category=category)
        # snacks = RecipeItem.objects.filter(category=category)
        # desserts = RecipeItem.objects.filter(category=category)
        # chuttney = RecipeItem.objects.filter(category=category)
        # curry = RecipeItem.objects.filter(category=category)
        # drinks = RecipeItem.objects.filter(category=category)
        # rice_dishes = RecipeItem.objects.filter(category=category)

         # Add everything to the context
        # context = {
        #     'category': category,
        #     'appetizers': appetizers,
        #     'snacks': snacks,
        #     'desserts': desserts,
        #     'chuttney': chuttney,
        #     'curry': curry,
        #     'drinks': drinks,
        #     'rice_dishes': rice_dishes,
        # }

        return render(request, 'customer/recipe_list.html', context)