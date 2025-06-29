from django.shortcuts import render, redirect
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
        'id_fornecedor'
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
                quantidade=peca.qtd_minima
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
