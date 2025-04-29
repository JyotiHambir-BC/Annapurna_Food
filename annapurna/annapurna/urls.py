

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer.views import Index, About, RecipeListView, RecipeCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('recipe/', RecipeListView.as_view(), name='recipe'),
    path('recipe/<slug:category_slug>', RecipeCategoryView.as_view(), name='recipe-category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

