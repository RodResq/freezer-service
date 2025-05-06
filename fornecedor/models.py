from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    contato = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'fornecedor'
        ordering = ['nome']
        verbose_name_plural = 'fornecedores'
