from django.contrib import admin
from .models import producteur, Representant

# Register your models here.

class producteurAdmin(admin.ModelAdmin):

    list_display = ('nom', 'adresse', 'telephone', 'representant')

admin.site.register(producteur)

class RepresentantAdmin(admin.ModelAdmin):

    list_display = ('nom')

admin.site.register(Representant)

