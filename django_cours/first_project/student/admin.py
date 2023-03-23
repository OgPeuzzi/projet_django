from django.contrib import admin
from .models import Student, Classe

# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    list_display = ('nom', 'prenom', 'classe', 'naissance', 'nom_pere', 'nom_mere', 'cycle')

admin.site.register(Student)

class ClasseAdmin(admin.ModelAdmin):

    list_display = ('classe')
admin.site.register(Classe)