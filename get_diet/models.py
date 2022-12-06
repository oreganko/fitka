from django.db import models


class DietDay(models.Model):
    date = models.DateField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.date)


class DayMeals(models.Model):
    diet_day = models.ForeignKey(DietDay, on_delete=models.CASCADE)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.diet_day) + ': ' + str(self.recipe)
