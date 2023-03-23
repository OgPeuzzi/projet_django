from django.db import models

# Create your models here.

class Driver(models.Model):

    nom = models.CharField(max_length=80)
    annee_experience = models.IntegerField()
    numero_permis = models.CharField(max_length=50)
    TYPE_PERMIS = [
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
    ]
    type_permis = models.CharField(choices= TYPE_PERMIS
                                     , default=1
                                     , max_length=5)
    BLOOD = [
        ('1', 'A+'),
        ('2', 'B+'),
        ('3', '0+'),
    ]
    groupe_sanguin = models.CharField(choices=BLOOD
                                      , default=1
                                      , max_length=5)

    vehicule = models.ForeignKey("vehicule.Vehicule", verbose_name="marque", on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Vehicule(models.Model):

    modele = models.ForeignKey("vehicule.Modele", verbose_name="modele", on_delete=models.CASCADE)
    numero_immatriculation = models.CharField(max_length=20)
    marque = models.CharField(max_length=100)
    nombre_place = models.IntegerField()
    marque = models.CharField(max_length=50)

    def __str__(self):
        return self.marque

class Modele(models.Model):

    modele = models.CharField(max_length=100)

    def __str__(self):
        return self.modele
