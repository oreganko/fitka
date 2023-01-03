from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('recipes/', views.add_recipe, name='add_recipe'),
]
