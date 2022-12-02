from django.db import models


class DietDay(models.Model):
    date = models.DateField()
    timestamp = models.DateTimeField()


class DayMeals(models.Model):
    diet_day = models.ForeignKey(DietDay, on_delete=models.CASCADE)
    recipe = models.ForeignKey('add_recipe.Recipe', on_delete=models.CASCADE)
