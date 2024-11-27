from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def str_response(request):
	return HttpResponse('This is a primitive function-based view to return a string reposnse')

def bioData(request):
			return HttpResponse('''
			<h1>Name: Shreelakshmi<h1>
			<i> Biodata <i>
			<b> Sub: Django <b>
			<img src = 'E://Parrot//DSC_0924.jpg'>''')
					   					   
