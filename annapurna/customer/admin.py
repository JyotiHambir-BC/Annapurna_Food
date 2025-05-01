from django.contrib import admin
from .models import RecipeItem, Category

@admin.register(RecipeItem)
class RecipeItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Show name and category columns in admin list view
    list_filter = ('category',)          # add a filter by category in the right sidebar
    search_fields = ('name',)            # enable search by recipe name


admin.site.register(Category)
