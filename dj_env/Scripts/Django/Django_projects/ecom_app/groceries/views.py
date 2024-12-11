from django.shortcuts import render
from django.http import HttpResponse

def staple(request):
    return HttpResponse('<h1>Display all the staple food items</h1>')

def spices(request):
    return HttpResponse('<h1> Display all the spices</h1>')
