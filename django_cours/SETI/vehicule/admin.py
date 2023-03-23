from django.contrib import admin
from .models import Driver, Modele, Vehicule

# Register your models here.

class DriverAdmin(admin.ModelAdmin):

        list_display = ('nom', 'annee_experience', 'numero_permis', 'TYPE_PERMIS', 'type_permis', 'BLOOD', 'groupe_sanguin','vehicule')

admin.site.register(Driver)

class VehiculeAdmin(admin.ModelAdmin):

    list_display = ('modele', 'numero_immatriculation', 'marque', 'nombre_place', 'carte grise')

admin.site.register(Vehicule)

class ModeleAdmin(admin.ModelAdmin):

    list_display = ('modele')

admin.site.register(Modele)
