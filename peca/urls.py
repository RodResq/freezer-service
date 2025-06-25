from django.urls import path
from .views import listar, cadastrar


app_name = 'peca'

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    # path('detalhar/<int:categoria_id>/', detalhar_peca, name="detalhar_categoria"),
    # path('editar/<int:categoria_id>/', editar_peca, name="editar_categoria"),
    # path('excluir/<int:categoria_id>/', excluir_peca, name="excluir_categoria")
]
