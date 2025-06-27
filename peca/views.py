from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PecaForm



def listar(request):
    return render(request, 'peca/form_peca.html')


@login_required
def cadastrar(request):
    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES)
        if form.is_valid():
            peca = form.save()
            messages.success(request, 'Peça armazenada com sucesso!')
            return redirect('local_armazenamento:listar')
    else:
        form = PecaForm()
        
    context = {
        'form': form,
        'titulo': 'Cadastrar Peça',
        'botao': 'Cadastrar',
        'icone': 'bi-plus-circle'
    }
    
    return render(request, 'peca/form_peca.html', context)
