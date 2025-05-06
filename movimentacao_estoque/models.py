from django.db import models
from peca.models import Peca

# Create your models here.
class MovimentacaoEstoque(models.Model):
    id_peca = models.ForeignKey(Peca, on_delete=models.DO_NOTHING, blank=False, null=False)
    tipo = models.CharField(max_length=200, blank=False, null=False)
    data_hora = models.DateTimeField(auto_now=True)
    quantidade = models.IntegerField()
    responsavel = models.CharField(max_length=100)
    
    
    class Meta:
        db_table = 'movimentacao_estoque'
        ordering = ['tipo']
        verbose_name_plural = 'movimentacoes_estoque'