from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def jewellery(request):
    return HttpResponse('<h1>Display all the jewelleries</h1>')

def outfits(request):
    return HttpResponse('<h1>Display all the outfits</h1>')
