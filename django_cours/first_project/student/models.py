from django.db import models

# Create your models here.

class Student(models.Model):

    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=200)
    # classe = models.CharField(max_length=50)
    classe = models.ForeignKey("student.Classe", verbose_name="classe",on_delete=models.CASCADE)
    cycle = models.CharField(max_length=50)
    nom_pere = models.CharField(max_length=40)
    nom_mere = models.CharField(max_length=40)
    naissance = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.nom
    
class Classe(models.Model):

    classe = models.CharField(max_length=50)

    def __str__(self):
        return self.classe
