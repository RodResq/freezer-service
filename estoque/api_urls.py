from django.urls import path
from . import api_views

urlpatterns = [
    path('buscar/', api_views.buscar, name='buscar'),
]