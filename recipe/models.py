from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Recipe(models.Model):
    TYPE_CHOICES = (
        ('ale','Ale'),
        ('lager','Lager'),
    )

    SUBTYPE_CHOICES = (
        ('Ale', (
            ('wheat ale', 'Wheat Ale'),
        )),
        ('Lager', (
            ('generic lager', 'Generic Lager'),  ## Change me
        ))
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='ale')
    subtype = models.CharField(max_length=50, choices=SUBTYPE_CHOICES, default='wheat ale')
    image = models.ImageField(null=True)
    default = models.BooleanField(default=False)
    creator = models.ForeignKey(User)

    ## Many to ones
    # Malt
    # Hop
    # Yeast


    def OG(self):
        pass


    def FG(self):
        pass


    def SRM(self):
        pass


    def IBU(self):
        pass


    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Malt(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    pass


class Hops(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    pass

class Yeast(models.Model):
    recipe = models.ForeignKey(Recipe)
    manufacturer = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    pass