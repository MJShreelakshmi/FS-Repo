from django.shortcuts import render

# Create your views here.
def if_elif_else(request):
    d = {'name':'Shree', 'age':12}
    return render(request, 'if_elif_else.html', d)