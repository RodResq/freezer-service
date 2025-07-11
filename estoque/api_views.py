from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Estoque


@require_http_methods(['GET'])
def buscar(request):
    pass