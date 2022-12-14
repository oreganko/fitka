# Generated by Django 4.0.6 on 2022-12-02 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_recipe', '0001_initial'),
        ('get_diet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='recipe',
        ),
        migrations.AlterField(
            model_name='daymeals',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_recipe.recipe'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
    ]
