from django.db import models

class Universitet(models.Model):
    nomi = models.CharField(max_length=255)  #  +
    manzil = models.CharField(max_length=255)  # +
    site =  models.CharField(max_length=255)  # code
    rektor = models.CharField(max_length=255)  # -
    contact = models.CharField(max_length=255) # -
    xorij_hamkorlik = models.CharField(max_length=255)  # -
    davlat = models.BooleanField(default=True) # -

    def __str__(self):
        return self.nomi


# Bino ma'lumotlari modeli
class Malumot(models.Model):
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE)
    fakultet = models.CharField(max_length=100)
    sigimi = models.CharField(max_length=255)
    ballar = models.CharField(max_length=255)
    reyting = models.CharField(max_length=255)
    konktrakt = models.CharField(max_length=255)

    def __str__(self):
        return self.reyting

