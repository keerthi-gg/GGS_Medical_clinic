from django.shortcuts import render


def home(request):
	return render(request, 'clinic/home.html')


def about(request):
	return render(request, 'clinic/about.html')


def services(request):
	return render(request, 'clinic/services.html')


def contact(request):
	return render(request, 'clinic/contact.html')
