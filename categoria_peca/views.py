from django.shortcuts import render
from django.contrib import messages
from .models import CategoriaPeca
from .forms import CategoriaPecaForm


# Create your views here.
def cadastrar_categoria(request):
    """
    Exibe o formulário para cadastrar uma nova categoria de peça
    """
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
