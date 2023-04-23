from django.shortcuts import render
from .forms import NotaFiscalForm

def criar_nota_fiscal(request):
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST)
        if form.is_valid():
            form.save()                       
    else:
        form = NotaFiscalForm()
    return render(request, 'criar_nota_fiscal.html', {'form': form})
