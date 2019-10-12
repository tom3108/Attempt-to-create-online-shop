from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_widok(*args, **kwargs):
	return HttpResponse("<h1> Sklep z używanymi akcesoriami komputerowymi</h1>") #String html