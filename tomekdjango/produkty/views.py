from django.shortcuts import render

from .forms import ProduktForm

from .models import Produkt

def produkt_utworz_widok (request):
	form = ProduktForm(request.POST or None)
	if form.is_valid():
		form.save(commit = True)
		form = ProduktForm()

	context = {
		'form' : form
	}
	return render (request, "produkt_utworz.html", context)


def opis (request):
	obj = Produkt.objects.get(id=3)
	kontekst = {
		'obiekt' : obj
	}
	return render (request, "opis.html", kontekst)
