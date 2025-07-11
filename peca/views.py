from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.files.base import ContentFile
from django.db.models import Q
from .models import Peca
from estoque.models import Estoque
from .forms import PecaForm
import os


@login_required
def listar(request):
    search = request.GET.get('search', '')
    categoria = request.GET.get('categoria', '')
    
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
        
    if categoria:
        pecas = pecas.filter(id_categoria_peca=categoria)
        
    pecas = pecas.order_by('nome')
    
    from categoria_peca.models import CategoriaPeca
    categorias = CategoriaPeca.objects.all().order_by('nome')
    
    context = {
        'pecas': pecas,
        'categorias': categorias,
        'search': search,
        'categoria_selecionada': categoria,
        'titulo': 'Peças Cadastradas'
    }
    
    return render(request, 'peca/listar_peca.html', context)


@login_required
def cadastrar(request):
    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES)
        if form.is_valid():
            peca = form.save()
            
            Estoque.objects.create(
                id_peca=peca,
                quantidade=peca.qtd_estoque
            )
            
            if peca.foto:
                extensao = os.path.splitext(peca.foto.name)[1]
                timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
                novo_nome = f"{peca.nome.replace(' ', '_')}_{peca.id}_{timestamp}{extensao}"
                
                conteudo_arquivo = peca.foto.read()
                
                if peca.foto:
                    peca.foto.delete(save=False)
                    
                peca.foto.save(novo_nome, ContentFile(conteudo_arquivo), save=True)
                    
            messages.success(request, 'Peça armazenada com sucesso!')
            return redirect('peca:listar')
    else:
        form = PecaForm()
        
    context = {
        'form': form,
        'titulo': 'Cadastrar Peça',
        'botao': 'Cadastrar',
        'icone': 'bi-plus-circle'
    }
    
    return render(request, 'peca/form_peca.html', context)


@login_required
def detalhar(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)
    
    context = {
        'peca': peca,
        'titulo': f'Detalhes da Peça: {peca.nome}'
    }
    
    return render(request, 'peca/detalhar_peca.html', context)


@login_required
def editar(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)
    
    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES, instance=peca)
        if form.is_valid():
            peca_editada = form.save()
            
            # Implementar Entrada em estoque das peças
            
            if 'foto' in request.FILES and peca_editada.foto:
                extensao_foto = os.path.splitext(peca_editada.foto.name)[1]
                timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
                nome_limpo = peca_editada.nome.replace(' ', '_').replace('/', '_').replace('\\', '_')
                nome_limpo = ''.join(c for c in nome_limpo if c.isalnum() or c in ('_', '-'))
                novo_nome = f"{nome_limpo}_{peca_editada.id}_{timestamp}{extensao_foto}"
                
                conteudo_arquivo_foto = peca_editada.foto.read()
                peca_editada.foto.delete(save=False)
                peca_editada.foto.save(novo_nome, ContentFile(conteudo_arquivo_foto), save=True)
                
            messages.success(request, 'Peça atualizada com sucesso!')
            return redirect('peca:listar')
    else:
        form = PecaForm(instance=peca)
        
    context = {
        'form': form,
        'titulo': 'Editar Peça',
        'botao': 'Atualizar',
        'icone': 'bi-pencil-square',
        'peca_id': peca_id
    }
    
    return render(request, 'peca/form_peca.html', context)


@login_required
def excluir(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)
    if request.method == 'POST':
        try:
            if peca.foto:
                peca.foto.delete()
                
            peca.delete()
            messages.success(request, 'Peça excluida com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao excluir peca {str(e)}')
        
        return redirect('peca:listar')
    
    context = {
        'peca': peca,
        'titulo': 'Confirmar Exclusão'
    }
        
    return render(request, 'peca/confirmar_exclusao.html', context)