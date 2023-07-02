from django.db import models

class Genus(models.Model):
    genus_name = models.CharField('Genus', max_length=150)
    image = models.ImageField(upload_to='blu_thumb/media/images/', default='default.jpg')
    geo_loc = models.CharField('Geographic Location(s)', max_length=255, default='')
    fav_eco = models.CharField('Favored Ecosystem(s)', max_length=255, default='') 
    
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
    