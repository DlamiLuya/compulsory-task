from django.db import models

# Create your models here.
# This will define the objects of the database where the recipes will be stored.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    ingrediants = models.TextField()
    method = models.TextField()
    date = models.DateField()
    bio = models.CharField(max_length=1000, null=True, blank=True)
    food_image=models.ImageField(null=True, blank=True)

def __str__(self):# The class string representation.
    return self.title