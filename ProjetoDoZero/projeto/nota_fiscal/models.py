from django.db import models

class NotaFiscal(models.Model):
    data_emissao = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)