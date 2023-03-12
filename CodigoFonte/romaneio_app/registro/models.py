from django.db import models

# Create your models here.

class Nota(models.Model):
    fornecedor = models.CharField('NOME_FORNECEDOR', max_length=50)
    razaosocial = models.CharField('RAZÃO_SOCIAL', max_length=50)
    nf = models.PositiveIntegerField('NF')
    mdeco = models.PositiveIntegerField('ORDEM_DE_COMPRA')
    dataEmissao = models.DateField('DATA_EMISSÃO', default=0)
    dataVencimento = models.DateField('DATA_VENCIMENTO', default=0)
    valor = models.DecimalField('VALOR', max_digits=8, decimal_places=2, default=0)
    dataEntrega = models.DateField('DATA_ENTREGA', default=0)
    recebedor = models.CharField('RECEBEDOR', max_length=200, blank=True, null=True)
    observacao = models.CharField('OBSERVAÇÃO', max_length=300, blank=True, null=True)

    class Meta:
        ordering=('fornecedor',)

    def __str__(self) :
        return self.fornecedor  

