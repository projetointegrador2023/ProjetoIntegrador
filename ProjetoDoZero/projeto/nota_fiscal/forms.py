from django import forms
from .models import NotaFiscal

class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = ['data_emissao', 'valor_total']