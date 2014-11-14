from django.shortcuts import render, get_object_or_404


# Create your views here.
from recipe.models import Recipe


def create(request):
    #recipes = Recipe.objects.all()
    return render(request,'create/create_recipe.html')
