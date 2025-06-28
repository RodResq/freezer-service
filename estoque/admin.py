from django.contrib import admin
from estoque.models import Estoque

# Register your models here.
@admin.register(Estoque)
class ListandoPecas(admin.ModelAdmin):
    list_display = ("id", "quantidade", "data_hora_atualizacao")
    ordering = ("id"), 
    list_per_page = 10  

# Register your models here.
