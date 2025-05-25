from django.urls import path
from .views import cadastrar_categoria

urlpatterns = [
    path('cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
]
