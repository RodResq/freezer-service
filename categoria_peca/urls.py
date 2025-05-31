from django.urls import path
from .views import cadastrar_categoria, listar_categorias, detalhar_categoria, editar_categoria, excluir_categoria

urlpatterns = [
    path('', listar_categorias, name='listar_categorias'),
    path('cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
    path('detalhar/<int:categoria_id>/', detalhar_categoria, name="detalhar_categoria"),
    path('editar/<int:categoria_id>/', editar_categoria, name="editar_categoria"),
    path('excluir/<int:categoria_id>/', excluir_categoria, name="excluir_categoria")
]
