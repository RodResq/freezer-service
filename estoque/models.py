from django.db import models
from peca.models import Peca

# Create your models here.
class Estoque(models.Model):
    id_peca = models.OneToOneField(Peca, on_delete=models.CASCADE, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True, default=0)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'estoque'
        verbose_name_plural = 'estoques'
        
    @property
    def quantidade_disponivel(self):
        return self.quantidade
    
    @property
    def status_estoque(self):
        if self.quantidade <= 0:
            return 'sem_estoque'
        elif self.quantidade <= self.id_peca.qtd_minima:
            return 'baixo'
        else:
            return 'normal'
    