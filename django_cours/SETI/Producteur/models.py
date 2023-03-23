from django.db import models

# Create your models here.

class producteur(models.Model):

    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    telephone = models.CharField(max_length=100)
    representant = models.ForeignKey("Producteur.Representant", verbose_name="representant", on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Representant(models.Model):

    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

