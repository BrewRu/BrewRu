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
            ('pale ale','Pale Ale'),('ipa','IPA'),('amber','Amber'),('brown','Brown'),('wheat ale', 'Wheat Ale'),('stout','Stout'),('belgian','Belgian')
        )),
        ('Lager', (
            ('light lager','Light Lager'),('hybrid lager','Hybrid Lager'),('bock', 'Bock'),  ## Change me
        ))
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='ale')
    subtype = models.CharField(max_length=50, choices=SUBTYPE_CHOICES, default='wheat ale')
    #yeast_pitch_rate = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(null=True)
    default = models.BooleanField(default=False)
    creator = models.ForeignKey(User, null=True)

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
    
    name = models.CharField(max_length=50)
   # amount = models.DecimalField(max_digits=10, decimal_places=3)
    country = models.CharField(max_length=50)
    color = models.IntegerField()
    gravity = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Hops(models.Model):
    
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    AAU = models.DecimalField(max_digits=10, decimal_places=1)


    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Yeast(models.Model):
    
    manufacturer = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    temp = models.DecimalField(max_digits=10, decimal_places=2)
    attenuation = models.DecimalField(max_digits=10, decimal_places=2)
    tolerance = models.DecimalField(max_digits=10, decimal_places=2)
    flocculation = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
		
		
		
class YeastIL(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.ForeignKey(Yeast)
    pitchrate = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name.name
		
class MaltIL(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.ForeignKey(Malt)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    
    

    def __str__(self):              # __unicode__ on Python 2
        return self.name.name


class HopsIL(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.ForeignKey(Hops)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.IntegerField()


    def __str__(self):              # __unicode__ on Python 2
        return self.name.name