from django.db import models

# Create your models here.
class Produkt(models.Model):
	nazwa = models.TextField()
	opis = models.TextField()
	cena = models.TextField()
	podsumowanie = models.TextField(default = 'Django to najlepszy framework')