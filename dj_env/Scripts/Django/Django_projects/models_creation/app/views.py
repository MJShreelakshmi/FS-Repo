from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn = input('Enter topic name: ')
    TOD = Topic.objects.get_or_create(topic_name = tn)
    if TOD[1]:
        return HttpResponse(f'{tn} object is newly created')
    else:
        return HttpResponse(f'{tn} already exists in the database')

def insert_webpage(request):
    tn = input('Enter topic name: ')
    n = input('Enter name: ')
    url = input('Enter url: ')
    LTO = Topic.objects.filter(topic_name = tn) # LTO --> List-Of Topic Objects
    if LTO:
        WTOD = Webpage.objects.get_or_create(topic_name = LTO[0], name = n, url = url)
        if WTOD[1]:
            return HttpResponse(f'A new webpage with <u>{url}</u> is created')
        else:
            return HttpResponse(f'A webpage with <u>{url}</u> already exists')
    else:
        return HttpResponse(f"{tn} doesn't exist in the database")
    
def insert_records(request):
    pk = int(input())
    a = input('Enter author: ')
    d = input('Enter date: ')
    LWO = Webpage.objects.filter(pk = pk)
    if LWO:
        RTOD = AccessRecords.objects.get_or_create(name = LWO[0], author = a, date = d )
        if RTOD[1]:
            return HttpResponse(f'A new webpage by {a} is created')
        else:
            return HttpResponse(f'A webpage by {a} already exists')
    else:
        return HttpResponse(f"{LWO[0]} doesn't exist in the database")