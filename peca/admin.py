from django.contrib import admin
from peca.models import Peca

# Register your models here.
@admin.register(Peca)
class ListandoPecas(admin.ModelAdmin):
    list_display = ("id", "nome", "codigo", "descricao", "qtd_minima", "qtd_estoque", "unidade", "foto", "valor", "id_categoria_peca", "id_local_armazenamento", "id_fornecedor")
    ordering = ("id"), 
    list_editable = ["qtd_minima", "qtd_estoque"]
    list_per_page = 10   