from django.shortcuts import render

# Create your views here.
def jinja_for(request):
    d = {'name': 'Shree', 'age':20}
    return render(request, 'for.html', {'d':d})