from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic

from recipes.models import Recipe


class RecipesListView(LoginRequiredMixin, generic.ListView):
    queryset = Recipe.objects.order_by('name')
    template_name = 'recipes/recipes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_views = self.request.session.get('num_visits', 0)
        context['num_visits'] = recent_views + 1
        self.request.session['num_visits'] = recent_views + 1
        return context


class RecipeView(LoginRequiredMixin, generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_ingredients'] = context['object'].recipeingredient_set.all()
        return context


def add_recipe(request):
    return HttpResponse('Adding recipe, help yourself...')
