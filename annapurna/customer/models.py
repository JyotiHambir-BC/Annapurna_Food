from django.db import models
from django.utils.text import slugify

class RecipeItem(models.Model):
    name = models.CharField(max_length=100)    
    image = models.ImageField(upload_to='recipe_images/')
    ingredients = models.TextField()
    how_to_make = models.TextField()
    required_time = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('category', related_name='recipe')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

