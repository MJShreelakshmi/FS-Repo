from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hotels(request):
    return HttpResponse('<h1> Display all the star hotels<h1>')

def restaurant(request):
    return HttpResponse('<h1>Display all the restaurants</h1>')