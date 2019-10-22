from django.shortcuts import render

from .models import Produkt

def opis (request):
	obj = Produkt.objects.get(id=3)
	kontekst = {
		'obiekt' : obj
	}
	return render (request, "opis.html", kontekst)
