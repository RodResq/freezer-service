from django.db import models

# Create your models here.
class CategoriaPeca(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        db_table = 'categoria_peca'
        ordering = ['nome']
        verbose_name_plural = 'categorias_pecas'