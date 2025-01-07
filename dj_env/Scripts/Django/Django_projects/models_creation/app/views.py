from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.

def insert_topic(request):
    tn = input('Enter topic name: ')
    TOD = Topic.objects.get_or_create(topic_name = tn)
    if TOD[1]:
        #return HttpResponse(f'{tn} object is newly created')
        LTO = Topic.objects.all()
        d = {'LTO':LTO}
        return render(request, 'display_topic.html',d)
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
            #return HttpResponse(f'A new webpage with <u>{url}</u> is created')
            LWO = Webpage.objects.all()
            d = {'LWO':LWO}
            return render(request, 'display_webpage.html', d)
        else:
            return HttpResponse(f'A webpage with <u>{url}</u> already exists')
    else:
        return HttpResponse(f"{tn} doesn't exist in the database")
    
def insert_records(request):
    try:
        pk =  int(input('Enter the id: '))
    except Exception as e:
        print(e)
    a = input('Enter author: ')
    d = input('Enter date: ')
    LWO = Webpage.objects.filter(pk = pk)
    if LWO:
        RTOD = AccessRecords.objects.get_or_create(name = LWO[0], author = a, date = d )
        if RTOD[1]:
            #return HttpResponse(f'A new webpage by {a} is created')
            LRO = AccessRecords.objects.all()
            d = {'LRO':LRO}
            return render(request, 'display_records.html', d)
        else:
            return HttpResponse(f'A webpage by {a} already exists')
    else:
        return HttpResponse(f"{LWO[0]} doesn't exist in the database")
    
def display_topic(request):
    LTO = Topic.objects.all()
    LTO = Topic.objects.order_by('-topic_name')
    LTO = Topic.objects.filter(topic_name__regex = '^\w?H')
    d = {'LTO':LTO}
    return render(request, 'display_topic.html',d)

def display_webpage(request):
    LWO = Webpage.objects.all()
    LWO = Webpage.objects.order_by(Length('url'), desc())
    # LWO = Webpage.objects.filter() 
    #try combining 2 or more functions together, use gt, gte, lt, lte etc  or name startswith and endswith
    d = {'LWO':LWO}
    return render(request, 'display_webpage.html', d)

def display_records(request):
    LRO = AccessRecords.objects.all()
    d = {'LRO':LRO}
    return render(request, 'display_records.html', d)