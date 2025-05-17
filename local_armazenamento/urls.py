from django.urls import path
from . import views

urlpatterns = [
     path('', views.listar_locais, name='listar_locais'),
     path('cadastrar/', views.cadastrar_local, name='cadastrar_local'),
     path('detalhar/<int:local_id>/', views.edtar_local_armazenamento, name='detalhar_local'),
     path('editar/<int:local_id>/', views.edtar_local_armazenamento, name='editar_local'),
     path('excluir/<int:local_id>/', views.excluir_local, name='excluir_local'),
]
