from django.http import HttpResponse


def hello_world(request):
	return HttpResponse('Hello World 9000')
	pass