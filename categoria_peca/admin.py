from django.contrib import admin
from categoria_peca.models import CategoriaPeca

# Register your models here.
@admin.register(CategoriaPeca)
class ListandoPecas(admin.ModelAdmin):
    list_display = ("nome",)
    list_per_page = 10  