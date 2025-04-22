

from django.contrib import admin
from django.urls import path, include
from customer.views import Index, About

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
]

