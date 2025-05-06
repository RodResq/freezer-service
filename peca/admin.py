from django.contrib import admin
from peca.models import Peca

# Register your models here.
@admin.register(Peca)
class ListandoPecas(admin.ModelAdmin):
    list_display = ("nome", "codigo", "descricao", "qtd_minima", "unidade")
    list_per_page = 10   