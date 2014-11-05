from django.contrib import admin

# Register your models here.
from recipe.models import Recipe, Malt, Yeast, Hops,MaltIL, YeastIL, HopsIL

@admin.register(Malt)
class Malt(admin.ModelAdmin):
    model = Malt


@admin.register(Hops)
class Hops(admin.ModelAdmin):
    model = Hops
  

@admin.register(Yeast)
class Yeast(admin.ModelAdmin):
    model = Yeast
   
	
class YeastInline(admin.TabularInline):
	model = YeastIL
	extra=1
	
class HopsInline(admin.TabularInline):
	model = HopsIL
	extra=1

class MaltInline(admin.TabularInline):
    model = MaltIL
    extra=1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Fields to be displayed in the individual admin page
    fieldsets = [
        (None, {'fields': ['name', 'type', 'subtype', 'default', 'creator']}),
    ]
    inlines = [MaltInline, HopsInline, YeastInline]
    #model=Recipe

    # Fields displayed for the list of items
    list_display = ('name', 'type', 'subtype', 'default', 'OG', 'FG', 'SRM', 'IBU')