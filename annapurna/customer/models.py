from django.db import models

class RecipeItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')
    required_time = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('category', related_name='recipe')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

