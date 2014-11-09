from django.contrib import admin

# Register your models here.
from recipe.models import Recipe, Malt, Yeast, Hops


class MaltInline(admin.TabularInline):
    model = Malt
    extra = 1


class HopsInline(admin.TabularInline):
    model = Hops
    extra = 1


class YeastInline(admin.TabularInline):
    model = Yeast
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Fields to be displayed in the individual admin page
    fieldsets = [
        (None, {'fields': ['name', 'type', 'subtype', 'default', 'creator']}),
    ]
    inlines = [MaltInline, HopsInline, YeastInline]

    # Fields displayed for the list of items
    list_display = ('name', 'type', 'subtype', 'default', 'OG', 'FG', 'SRM', 'IBU')