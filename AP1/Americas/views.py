from django.shortcuts import render

# Create your views here.

def americas(request):
	return render(request, 'americas.html')

def canada(request):
	return render(request, 'canada.html')
	
def colombia(request):
	return render(request, 'colombia.html')
	
def mexico(request):
	return render(request, 'mexico.html')
