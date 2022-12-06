from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipes/', views.add_recipe, name='add_recipe'),
]
