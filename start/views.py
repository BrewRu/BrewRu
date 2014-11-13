from django.shortcuts import render, get_object_or_404


# Create your views here.
from recipe.models import Recipe


def start(request):
    #recipe = get_object_or_404(klass=Recipe, pk=recipe_id)
    return render(request,'start/start.html')



def equipment(request):
    #recipe = get_object_or_404(klass=Recipe, pk=recipe_id)
    return render(request,'start/equipment.html')
