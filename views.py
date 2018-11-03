from django.http import HttpRsponse

def index(request):
	return HttpResponse("ok")

def login(request):
	return HttpResponse("yes")

def register(request):
	return HttpResponse("yes")
