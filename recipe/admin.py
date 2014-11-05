from django.contrib import admin

# Register your models here.
from recipe.models import Recipe, Malt, Yeast, Hops

@admin.register(Malt)
class Malt(admin.ModelAdmin):
    model = Malt
    extra = 1

@admin.register(Hops)
class Hops(admin.ModelAdmin):
    model = Hops
    extra = 1

@admin.register(Yeast)
class Yeast(admin.ModelAdmin):
    model = Yeast
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Fields to be displayed in the individual admin page
  #  fieldsets = [
   #     (None, {'fields': ['name', 'type', 'subtype', 'default', 'creator']}),
    #]
    model=Recipe

    # Fields displayed for the list of items
    list_display = ('name', 'type', 'subtype', 'default', 'OG', 'FG', 'SRM', 'IBU')