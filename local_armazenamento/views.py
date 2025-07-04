from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import LocalArmazenamento
from .forms import LocalArmazenamentoForm
# Create your views here.

@login_required
def listar(request):
    search = request.GET.get('search', '')
    locais = LocalArmazenamento.objects.all()
    
    if search:
        locais = locais.filter(
            Q(setor__icontains=search) |
            Q(estante__icontains=search) |
            Q(prateleira__icontains=search) |
            Q(descricao__icontains=search)
        )
    
    locais = locais.order_by('setor', 'estante', 'prateleira')
    
    context = {
        'locais': locais,
        'titulo': 'Locais de Armazenamento'
    }
    
    return render(request, 'local_armazenamento/listar_locais.html', context)
    
    
@login_required
def detalhar(request, local_id):
    local = get_object_or_404(LocalArmazenamento, pk=local_id)
    
    parte_titulo = []
    if local.setor:
        parte_titulo.append(local.setor)
    if local.estante:
        parte_titulo.append(f"Est. {local.estante}")
    if local.prateleira:
        parte_titulo.append(f"Prat, {local.prateleira}")
        
    titulo = f"Detalhes do Local: {' - '.join(parte_titulo)}" if parte_titulo else "Detalhes do Local"
    
    context = {
        'local': local,
        'titulo': titulo
    }
    return render(request, 'local_armazenamento/detalhar_local.html', context)


@login_required
def cadastrar(request):
    if request.method == 'POST':
        form = LocalArmazenamentoForm(request.POST)
        if form.is_valid():
            local = form.save()
            
            local_info = []
            if local.setor:
                local_info.append(f"Setor: {local.setor}")
            if local.estante:
                local_info.append(f"Estante: {local.estante}")
            if local.prateleira:
                local_info.append(f"Prateleira: {local.prateleira}")
            
            mensagem = f"Local de armazenamento cadastrado com sucesso!"
            if local_info:
                mensagem += f" ({' - '.join(local_info)})"
                
            return redirect('local_armazenamento:listar')
    else:
        form = LocalArmazenamentoForm()
            
    context = {
        'form': form,
        'titulo': 'Cadastrar Local de Armazenamento',
        'botao': 'Cadastrar',
        'icone': 'bi-plus-circle'
    }
    
    return render(request, 'local_armazenamento/form_local.html', context)
    

@login_required
def editar(request, local_id):
    local = get_object_or_404(LocalArmazenamento, pk=local_id)
    
    if request.method == 'POST':
        form = LocalArmazenamentoForm(request.POST, instance=local)
        
        if form.is_valid():
            local_atualizado = form.save()
            local_info = []
            
            if local_atualizado.setor:
                local_info.append(f"Setor: {local_atualizado.setor}")
            if local_atualizado.estante:
                local_info.append(f"Estante: {local_atualizado.estante}")
            if local_atualizado.prateleira:
                local_info.append(f"Prateleira: {local_atualizado.prateleira}")
            
            mensagem = f"Local de armazenamento atualizado com sucesso!"
            
            if local_info:
                mensagem += f" ({' - '.join(local_info)})"
            
            messages.success(request, mensagem)
            return redirect('local_armazenamento:listar')
    else:
        form = LocalArmazenamentoForm(instance=local)
        
    context = {
        'form': form,
        'titulo': 'Editar Local de Armazenamento',
        'botao': 'Atualizar',
        'icone': 'bi-pencil-square',
        'local_id': local_id
    }
    
    return render(request, 'local_armazenamento/form_local.html', context)
    
@login_required
def excluir(request, local_id):
    local = get_object_or_404(LocalArmazenamento, pk=local_id)
    
    if request.method == 'POST':
        try:
            qtd_pecas_associadas = local.peca_set.count()
            
            if qtd_pecas_associadas > 0:
                messages.error(
                    request, 
                    f'Não é possível excluir este local pois existem {qtd_pecas_associadas} '
                    f'peça{"s" if qtd_pecas_associadas > 1 else ""} associada{"s" if qtd_pecas_associadas > 1 else ""} a ele.'
                )
                return redirect('local_armazenamento:listar')
            
            local_info = []
            if local.setor:
                local_info.append(f"Setor: {local.setor}")
            if local.estante:
                local_info.append(f"Estante: {local.estante}")
            if local.prateleira:
                local_info.append(f"Prateleira: {local.prateleira}")
                
            mensagem = f"Local de armazenamento excluído com sucesso!"
            if local_info:
                mensagem += f" ({' - '.join(local_info)})"   
                
            local.delete()
            messages.success(request, mensagem)
            
        except Exception as e:
            messages.error(request, f'Erro ao excluir local de armazenamento: {str(e)}')
            
        return redirect('local_armazenamento:listar')
    
    context = {
        'local': local,
        'titulo': 'Confirmar Exclusão'
    }
    
    return render(request, 'local_armazenamento/confirmar_exclusao.html', context)