from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from recipes.models import Recipe


def index(request):
    return HttpResponse(render(request, 'recipes/index.html'))


def recipe(request, recipe_id=1):
    given_recipe = Recipe.objects.get(id=recipe_id)
    recipe_ingredients = given_recipe.ingredients.through.objects.all()
    context = {
        'recipe': given_recipe,
        'recipe_ingredients': recipe_ingredients
    }
    return HttpResponse(render(request, 'recipes/recipe.html', context))


def add_recipe(request):
    return HttpResponse('Adding recipe, help yourself...')

