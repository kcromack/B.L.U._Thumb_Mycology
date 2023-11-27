from django.db import models
from multiselectfield import MultiSelectField

class Genus(models.Model):
    genus_name = models.CharField('Genus', max_length=150)
    image = models.ImageField(upload_to='media/images/', default='default.jpg')
    GEO_LOC_CHOICES = [
        ('Africa', 'Africa'),
        ('Antarctica', 'Antarctica'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Oceania', 'Oceania'),
        ('South America', 'South America'),
    ]
    geo_loc = MultiSelectField('Geographic Location(s)', choices=GEO_LOC_CHOICES, max_choices=7, max_length=255, default=[])
    FAV_ECO_CHOICES = [
        ('Alpine', 'Alpine'),
        ('Coastal', 'Coastal'),
        ('Desert', 'Desert'),
        ('Forest', 'Forest'),
        ('Grassland', 'Gassland'),
        ('Urban', 'Urban'),
        ('Wetland', 'Wetland'),
    ]
    fav_eco = MultiSelectField('Favored Ecosystem(s)', choices=FAV_ECO_CHOICES, max_choices=7, max_length=255, default=[])
    SUB_PREF_CHOICES = [
        ('Compost', 'Compost'),
        ('Grain', 'Grain'),
        ('Manure', 'Manure'),
        ('Straw', 'Straw'),
        ('Wood', 'Wood'),
    ]
    sub_pref = MultiSelectField('Substrate Preference(s)', choices=SUB_PREF_CHOICES, max_choices=5, max_length=255, default=[])
    HOST_TREES_CHOICES = [
        ('Deciduous', 'Deciduous'),
        ('Coniferous', 'Coniferous'),
    ]
    host_trees = MultiSelectField('Host Trees', choices=HOST_TREES_CHOICES, max_choices=2, max_length=255, default=[])

    def __str__(self):
        return self.genus_name
    
    class Meta:
        verbose_name_plural = 'Genera'

class Species(models.Model):
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    species_name = models.CharField('Species', max_length=150)
    image = models.ImageField(upload_to='blu_thumb/media/images/', default='default.jpg')
    geo_loc = models.CharField('Geographic Location(s)', max_length=255, default='')
    fav_eco = models.CharField('Favored Ecosystem(s)', max_length=255, default='') 
    choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    indoor_cultivation = models.CharField(max_length=3, choices=choices, default='yes')
    medicinal = models.CharField(max_length=3, choices=choices, default='no')  
    
    def __str__(self):
        return self.species_name
    
    class Meta:
        verbose_name_plural = 'Species'

class Variety(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    variety_name = models.CharField('Variety', max_length=150)
    image = models.ImageField(upload_to='blu_thumb/media/images/', default='default.jpg')

    def __str__(self):
        return self.variety_name

    class Meta:
        verbose_name_plural = 'Variety'

    #class Meta:
        #ordering = ['Genus', 'Species', 'Variety']
    