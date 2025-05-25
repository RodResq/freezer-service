from django import forms
from .models import CategoriaPeca

class CategoriaPecaForm(forms.ModelForm):
    
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome da categoria'
        }),
        error_messages={
            'required': 'O nome da categoria é obrigatório.',
        }
    )
    
    class Meta:
        model = CategoriaPeca
        fields = ['nome']
        
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome:
            nome = nome.strip().title()
            
            existe_categoria = CategoriaPeca.objects.filter(nome__iexact=nome)
            if self.instance.pk:
                existe_categoria = existe_categoria.exclude(pk=self.instance.pk)
                
            if existe_categoria.exists():
                raise forms.ValidationError('Já existe uma categoria com este nome.')
        
        return nome