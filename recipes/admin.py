from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient, Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = [('name', 'calories', 'cooking_time_minutes'), 'meal',
              'author', 'public']


admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)
