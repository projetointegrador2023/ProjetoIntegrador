from django.shortcuts import render

def funcao_index(request):
    return render(request, 'index.html')