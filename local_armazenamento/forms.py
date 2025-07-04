from django import forms
from .models import LocalArmazenamento

class LocalArmazenamentoForm(forms.ModelForm):
    
    setor = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Setor'})
    )
    
    estante = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estante'})
    )
    
    prateleira = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prateleira'})
    )
    
    cor_referencia = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color',
            'title': 'Selecione uma cor de referência'
        }),
        help_text='Selecione uma cor para identificar visualmente este local'
    )
    
    descricao = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição', 'rows': 3 })
    )
    
    class Meta:
        model = LocalArmazenamento
        fields = ['setor', 'estante', 'prateleira', 'cor_referencia', 'descricao']