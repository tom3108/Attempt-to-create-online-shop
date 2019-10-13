from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_widok(*args, **kwargs):
	return HttpResponse("<h1> Sklep z używanymi akcesoriami komputerowymi</h1>") #String html
def kontakt(*args, **kwargs):
	return HttpResponse("<h1> Kontakt mailowy: t.madziara@gmail.com </h1>") #String html
def oNas(*args, **kwargs):
	return HttpResponse("<h1> Sklep z 20 letnią historią </h1>") #String html
def media(*args, **kwargs):
	return HttpResponse("<h1> Facebook, Instagram, Twitter </h1>") #String html