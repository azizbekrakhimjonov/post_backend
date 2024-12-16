from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=255)  #  +
    manzil = models.CharField(max_length=255)  # +
    code =  models.CharField(max_length=255)  # code

    def __str__(self):
        return self.nomi


# Bino ma'lumotlari modeli
class Malumot(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=100)
    qoyida = models.CharField(max_length=255)


    def __str__(self):
        return self.nomi

