from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_widok(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render (request, "dom.html", {})
def kontakt(request, *args, **kwargs):
	return render (request, "kontakt.html", {})
def oNas(request, *args, **kwargs):
	kontekst = {
		"data":"otwarcie sklepu: maj 1997",
		"liczba":"szacunkowa ilość klientów na dzień: 135",
		"kody" : [12,14,16,17,18]
	}
	return render (request, "onas.html", kontekst)
def media(request, *args, **kwargs):
	return HttpResponse("<h1> Facebook, Instagram, Twitter </h1>") #String html