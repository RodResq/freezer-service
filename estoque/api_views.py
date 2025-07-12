from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from peca.models import Peca


@require_http_methods(['GET'])
def buscar(request):
    search = request.GET.get('search', '').strip()
    
    pecas = Peca.objects.select_related(
        'id_categoria_peca',
        'id_local_armazenamento',
        'id_fornecedor',
        'estoque'
    ).all()
    
    if search:
        pecas = pecas.filter(
            Q(nome__icontains=search) |
            Q(codigo__icontains=search) |
            Q(descricao__icontains=search)
        )
        
    pecas = pecas.order_by('nome')
    
    pecas_data = list(pecas.values(
        'id', 
        'codigo', 
        'nome', 
        'id_local_armazenamento__prateleira', 
        'id_local_armazenamento__estante',  
        'id_local_armazenamento__setor', 
        'id_local_armazenamento__cor_referencia', 
        'estoque__quantidade'
    ))
    
    return JsonResponse({
        'success': True,
        'pecas': pecas_data
    })