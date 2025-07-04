from django.contrib import admin
from local_armazenamento.models import LocalArmazenamento


@admin.register(LocalArmazenamento)
class ListandoLocaisArmazenamento(admin.ModelAdmin):
    list_display = ("id", "setor", "estante", "prateleira", "cor_referencia", "descricao")
    ordering = ("id"), 
    list_per_page = 10   
# Register your models here.
