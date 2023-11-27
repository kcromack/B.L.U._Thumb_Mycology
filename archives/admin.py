from django.contrib import admin

from .models import Genus, Species, Variety

admin.site.register(Genus)
admin.site.register(Species)
admin.site.register(Variety)

