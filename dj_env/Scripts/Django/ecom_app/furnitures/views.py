from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dining(request):
    return HttpResponse('<h1>Display all the dining sets</h1>')

def sofaset(request):
    return HttpResponse('<h1>Display all the Sofa sets</h1>')