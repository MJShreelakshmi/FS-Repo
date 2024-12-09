from django.shortcuts import render

# Create your views here.
def if_elif(request):
    d = {'name':'Shree', 'age':16}
    return render(request, 'if_elif.html', d)