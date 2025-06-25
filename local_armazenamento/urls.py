from django.urls import path
from . import views


app_name = 'local_armazenamento'

urlpatterns = [
     path('', views.listar, name='listar'),
     path('cadastrar/', views.cadastrar, name='cadastrar'),
     path('detalhar/<int:local_id>/', views.detalhar, name='detalhar'),
     path('editar/<int:local_id>/', views.editar, name='editar'),
     path('excluir/<int:local_id>/', views.excluir, name='excluir'),
]
