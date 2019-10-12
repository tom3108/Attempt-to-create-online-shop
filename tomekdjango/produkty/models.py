from django.db import models

# Create your models here.
class Produkt(models.Model):
	nazwa = models.TextField()
	opis = models.TextField(blank=True, null=True)
	cena = models.DecimalField(max_digits=10000, decimal_places=2)
	podsumowanie = models.TextField(default = 'Django to najlepszy framework')
	przecena = models.BooleanField()
