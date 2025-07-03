from django.urls import path
from .views import listar, cadastrar, detalhar, editar, excluir


app_name = 'peca'

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('detalhar/<int:peca_id>/', detalhar, name="detalhar"),
    path('editar/<int:peca_id>/', editar, name="editar"),
    path('excluir/<int:peca_id>/', excluir, name="excluir")
]
