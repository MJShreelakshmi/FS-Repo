from django.shortcuts import render

# Create your views here.
def parrot(request):
    return render(request, 'parrot.html')