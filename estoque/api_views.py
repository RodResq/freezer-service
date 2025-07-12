from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from peca.models import Peca


@require_http_methods(['GET'])
def buscar(request):
    pecas = Peca.objects.select_related(
        'id_categoria_peca',
        'id_local_armazenamento',
        'id_fornecedor',
        'estoque'
    ).all()
    
    pecas_data = list(pecas.values(
        'id', 'codigo', 'nome', 'id_local_armazenamento__setor', 'estoque__quantidade'
    ))
    
    return JsonResponse({
        'success': True,
        'pecas': pecas_data
    })