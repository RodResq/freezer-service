from django.urls import path
from .views import cadastrar, listar, detalhar, editar, excluir


app_name = 'categoria_peca'

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('detalhar/<int:categoria_id>/', detalhar, name="detalhar"),
    path('editar/<int:categoria_id>/', editar, name="editar"),
    path('excluir/<int:categoria_id>/', excluir, name="excluir")
]
