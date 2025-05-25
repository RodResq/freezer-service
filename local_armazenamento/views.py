from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LocalArmazenamento
from .forms import LocalArmazenamentoForm
# Create your views here.

# @login_required
def listar_locais(request):
    """
    Exibe a lista de todos os locais de armazenamento cadastrados
    """
    locais = LocalArmazenamento.objects.all().order_by('setor', 'estante', 'prateleira')
    context = {
        'locais': locais,
        'titulo': 'Locais de Armazenamento'
    }
    
    return render(request, 'local_armazenamento/listar_locais.html', context)
    
    
@login_required
def detalhar_local(request, local_id):
    """
        Exibe os detalhes de um local de armazenamento específico
    """
    local = get_object_or_404(LocalArmazenamento, pk=local_id)
    context = {
        'local': local,
        'titulo': f'Detalhes do Local: {local.setor} - {local.estante}'
    }
    return render(request, 'local_armazenamento/detalhar_local.html', context)

@login_required
def cadastrar_local(request):
    """
        Exibe o formulário para cadastrar um novo local de armazenamento
    """
    if request.method == 'POST':
        form = LocalArmazenamentoForm(request.POST)
        if form.is_valid():
            local = form.save()
            messages.success(request, 'Local de armazenamento cadastrado com sucesso!')
            return redirect('listar_locais')
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
def editar_local_armazenamento(request, local_id):
    """
        Exibe o formulário para editar um local de armazenamento existente
    """
    local = get_object_or_404(LocalArmazenamento, pk=local_id)
    
    if request.method == 'POST':
        form = LocalArmazenamentoForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            messages.success(request, 'Local de armazenamento atualizado com sucesso!')
            return redirect('listar_locais')
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
def excluir_local(request, local_id):
    """
        Exclui um local de armazenamento
    """
    local = get_object_or_404(LocalArmazenamento, pk=local_id)
    
    if request.method == 'POST':
        try:
            local.delete()
            messages.success(request, 'Local de armazenamento excluído com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao excluir local de armazenamento: {str(e)}')
        return redirect('listar_locais')
    
    context = {
        'local': local,
        'titulo': 'Confirmar Exclusão'
    }
    
    return render(request, 'local_armazenamento/confirmar_exclusao.html', context)