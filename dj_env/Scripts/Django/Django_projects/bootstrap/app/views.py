from django.shortcuts import render

# Create your views here.
def test_img(request):
    return render(request, 'test_img.html')
    