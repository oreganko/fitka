from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    class MealTime(models.TextChoices):
        BREAKFAST = 'Breakfast'
        SECOND_BREAKFAST = 'Second breakfast'
        LUNCH = 'Lunch'
        ELEVENSES = 'Elevenses'
        SUPPER = 'Supper'
        SNACK = 'Snack'

    name = models.CharField(max_length=70)
    calories = models.IntegerField(default=0)
    cooking_time_minutes = models.IntegerField(default=0)
    meal = models.CharField(max_length=20,
                            choices=MealTime.choices,
                            default=MealTime.BREAKFAST)
    preparation = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient')
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.id)])


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    amount_unit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.recipe} \n\t{self.ingredient} - {self.amount} {self.amount_unit}'
