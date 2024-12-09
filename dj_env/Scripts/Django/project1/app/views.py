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
			<img src = 'https://www.freepik.com/premium-ai-image/young-girl-hr-3d-character-young-working-girl-cartoon-character-professional-girl-character_79639230.htm'>''')
					   					   
