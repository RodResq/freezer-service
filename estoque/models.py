from django.db import models
from peca.models import Peca

# Create your models here.
class Estoque(models.Model):
    id_peca = models.ForeignKey(Peca, on_delete=models.CASCADE, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True, default=0)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'estoque'
        verbose_name_plural = 'estoques'
    