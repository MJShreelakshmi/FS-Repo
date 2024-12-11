from django.shortcuts import render

# Create your views here.
def dynamic_path(request):
    return render(request, 'path.html')