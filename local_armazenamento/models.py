from django.db import models

# Create your models here.
class LocalArmazenamento(models.Model):
    setor = models.CharField(max_length=200, blank=True, null=True)
    estante = models.CharField(max_length=50, blank=True, null=True)
    prateleira = models.CharField(max_length=50, blank=True, null=True)
    cor_referencia = models.CharField(max_length=7, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'local_armazenamento'
        ordering = ['setor']
        verbose_name_plural = 'locais_armazenamento'
        
    def __str__(self):
        return self.setor
    
