from django.shortcuts import render, get_object_or_404


# Create your views here.
from recipe.models import Recipe


def view_recipe(request, recipe_id):
    recipe = get_object_or_404(klass=Recipe, pk=recipe_id)
    return render(request,
                  'recipe/viewrecipe.html',
                  {
                      'recipe': recipe,
                  })


def view_all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request,
                  'recipe/viewallrecipes.html',
                  {
                      'recipes': recipes,
                  })

def brewmaster(request, recipe_id):
    recipe = get_object_or_404(klass=Recipe, pk=recipe_id)
    return render(request,
                  'recipe/brewmaster.html',
        {
            'recipe': recipe,
        })