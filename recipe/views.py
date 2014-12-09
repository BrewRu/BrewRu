from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from recipe.forms import *
from recipe.models import Recipe


FORMS = [("recipe", RecipeForm),
         ("malt", modelformset_factory(MaltIL, formset=MaltFormSet, extra=3, exclude=["recipe"])),
         ("hops", modelformset_factory(HopsIL, formset=HopsFormSet, extra=3, exclude=["recipe"])),
         ("yeast", modelformset_factory(YeastIL, formset=YeastFormSet, extra=3, exclude=["recipe"]))]


class RecipeWizard(SessionWizardView):
    template_name = "recipe/recipe_wizard.html"

    def save_recipe(self, form_dict):
        recipe = form_dict['recipe'].save()
        malts = form_dict['malt'].save(commit=False)
        hopss = form_dict['hops'].save(commit=False)
        yeasts = form_dict['yeast'].save(commit=False)
        for malt in malts:
            malt.recipe = recipe
            malt.save()
        for hops in hopss:
            hops.recipe = recipe
            hops.save()
        for yeast in yeasts:
            yeast.recipe = recipe
            yeast.save()
        return recipe

    def done(self, form_list, form_dict, **kwargs):
        recipe = self.save_recipe(form_dict)
        return HttpResponseRedirect(reverse('view_recipe', args=[recipe.id]))


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