from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=70)
    calories = models.IntegerField(default=0)
    cooking_time_minutes = models.IntegerField(default=0)
    meal = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient')
    )

    def __str__(self):
        return (f'{self.name} - {self.meal} ({self.calories} kcal, {self.cooking_time_minutes} min)' +
                '\n\t' +
                '\n\t'.join([str(ingredient.ingredient) + ' ' + str(ingredient.amount) + ' ' + ingredient.amount_unit
                             for ingredient in self.ingredients.through.objects.all()])
                )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    amount_unit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.recipe} \n\t{self.ingredient} - {self.amount} {self.amount_unit}'
