from django.shortcuts import render

# Create your views here.
def home1(request):
    return render(request, 'app1/home1.html')

def login1(request):
    return render(request, 'app1/child1.html')