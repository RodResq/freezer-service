from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CategoriaPeca
from .forms import CategoriaPecaForm



@login_required
def listar_categorias(request):
    search = request.GET.get('search', '')
    categorias = CategoriaPeca.objects.all()
    
    if search:
        categorias = categorias.filter(nome__icontains=search)
        
    categorias = categorias.order_by('nome')
    
    context = {
        'categorias': categorias,
        'titulo': 'Categorias de Peça',
        'search': search
    }
    
    return render(request, 'categoria_peca/listar_categoria.html', context)


def detalhar_categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaPeca, pk=categoria_id)
    total_pecas = categoria.peca_set.count()
    
    context = {
        'categoria': categoria,
        'total_pecas': total_pecas,
        'titulo': f'Detalhes da Categoria: {categoria.nome}'
    }
    
    return render(request, 'categoria_peca/detalhar_categoria.html', context)


@login_required
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaPecaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, 'Categoria de peça cadastrada com sucesso!')
    else:
        form = CategoriaPecaForm()
        
    context = {
        'form': form,
        'titulo': 'Cadastrar Categoria de Peça',
        'botao': 'Cadastrar',
        'icone': 'bi-plus-circle'
    }
    
    return render(request, 'categoria_peca/form_categoria.html', context)

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaPeca, pk=categoria_id)
    
    if request.method == 'POST':
        form = CategoriaPecaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria de peça atualizada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaPecaForm(instance=categoria)
        
    context = {
        'form': form,
        'titulo': 'Editar Categoria de Peça',
        'botao': 'Atualizar',
        'icone': 'bi-pencil-square',
        'categoria_id': categoria_id
    }
    
    return render(request, 'categoria_peca/form_categoria.html', context)


@login_required
def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaPeca, pk=categoria_id)
    pecas_associadas = categoria.peca_set.count()
    
    if request.method == 'POST':
        if pecas_associadas > 0:
            messages.error(request, f'Não é possível excluir esta categoria pois existem {pecas_associadas} peça(s) associada(s) a ela.')
            return redirect('listar_categorias')
        
        try:
            categoria.delete()
            messages.success(request, 'Categoria de peça excluída com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao excluir categoria: {str(e)}')
        return redirect('listar_categorias')
    
    context = {
        'categoria': categoria,
        'pecas_associadas': pecas_associadas,
        'titulo': 'Confirmar Exclusão'
    }
    
    return render(request, 'categoria_peca/confirmar_exclusao.html', context)
