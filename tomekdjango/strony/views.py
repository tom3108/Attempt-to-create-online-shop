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
	return render (request, "onas.html", {})
def media(request, *args, **kwargs):
	return HttpResponse("<h1> Facebook, Instagram, Twitter </h1>") #String html