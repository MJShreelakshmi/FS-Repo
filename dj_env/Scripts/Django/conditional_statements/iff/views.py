from django.shortcuts import render

# Create your views here.
def jinja_if(request):
    d = {'name':'Shree', 'age':4}
    return render(request, 'jinja_if.html', d)