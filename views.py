from django.http import HttpRsponse

def index(request):
	return HttpResponse("ok")
