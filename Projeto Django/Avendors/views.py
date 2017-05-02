from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.forms import form

# Create your views here.

def index(request):
	return render(request, "index.html")

def parceiros(request):
	return render(request, "parceiros.html")

def contato(request):
	return render(request, "contato.html")

def login(request):
	return render(request, "login.html")

def newuser(request):
	return render(request, "newuser.html")

def barcos(request):
	return render(request, "barcos.html")
'''def newuser(request):
	if request.method == 'POST':
		form = ModelForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponse("/login/")
		else:
			return render(request, "newuser.html", {"form": form})

	return render(request, "newuser.html",{"form": ModelForm()})'''




