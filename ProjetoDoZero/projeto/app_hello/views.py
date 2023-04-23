from django.http import HttpResponse

def funcao_hello(request):
    return HttpResponse("Hello World")