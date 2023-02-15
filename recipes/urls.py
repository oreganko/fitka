from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='index'),
    path('<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
]
