__author__ = 'rbonick'

from django.forms import ModelForm, BaseModelFormSet
from recipe.models import Recipe, MaltIL, YeastIL, HopsIL


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'type', 'subtype']


class MaltFormSet(BaseModelFormSet):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
             queryset=None, **kwargs):
        queryset = MaltIL.objects.none()
        super(MaltFormSet, self).__init__(data, files,
            auto_id, prefix, queryset, **kwargs)

class HopsFormSet(BaseModelFormSet):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
             queryset=None, **kwargs):
        queryset = HopsIL.objects.none()
        super(HopsFormSet, self).__init__(data, files,
            auto_id, prefix, queryset, **kwargs)

class YeastFormSet(BaseModelFormSet):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
             queryset=None, **kwargs):
        queryset = YeastIL.objects.none()
        super(YeastFormSet, self).__init__(data, files,
            auto_id, prefix, queryset, **kwargs)

class MaltForm(ModelForm):
    class Meta:
        model = MaltIL
        fields = ['name', 'amount']

class YeastForm(ModelForm):
    class Meta:
        model = YeastIL
        fields = ['name', 'pitchrate']

class HopsForm(ModelForm):
    class Meta:
        model = HopsIL
        fields = ['name', 'amount', 'time']