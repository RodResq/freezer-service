from django.db import models
from categoria_peca.models import CategoriaPeca
from local_armazenamento.models import LocalArmazenamento
from fornecedor.models import Fornecedor

# Create your models here.

class Peca(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    codigo = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.TextField(max_length=500, blank=False, null=False)
    qtd_minima = models.IntegerField(blank=True, null=True, default=0)
    unidade = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="foto/%Y/%m/%d/", blank=True)
    id_categoria_peca = models.ForeignKey(CategoriaPeca, on_delete=models.CASCADE, blank=False, null=False)
    id_local_armazenamento = models.ForeignKey(LocalArmazenamento, on_delete=models.SET_NULL, blank=True, null=True)
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    class Meta:
        db_table = 'peca'
        ordering = ['nome',]
        verbose_name_plural = 'pecas'
    
