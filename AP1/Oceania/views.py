from django.shortcuts import render

# Create your views here.

def oceania(request):
	return render(request, 'oceania.html')

def novazelandia(request):
	return render(request, 'novazelandia.html')
	
def australia(request):
	return render(request, 'australia.html')
