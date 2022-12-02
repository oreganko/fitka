from django.db import models


class Recipe(models.Model):
    calories = models.IntegerField(default=0)
    cooking_time_minutes = models.IntegerField(default=0)
    meal = models.CharField(max_length=30)


class Ingredient(models.Model):
    name = models.CharField(max_length=40)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    amount_unit = models.CharField(max_length=10)
