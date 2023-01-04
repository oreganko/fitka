from django.http import HttpResponse
from django.views import generic

# Create your views here.
from recipes.models import Recipe


class IndexView(generic.ListView):
    queryset = Recipe.objects.order_by('name')
    template_name = 'recipes/recipes_list.html'


class RecipeView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_ingredients'] = context['object'].recipeingredient_set.all()
        return context


def add_recipe(request):
    return HttpResponse('Adding recipe, help yourself...')
