from django import forms
from .models import Peca


class PecaForm(forms.ModelForm):
    
    class Meta:
        model = Peca
        fields = ['nome', 'codigo', 'descricao', 'qtd_minima', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            
            'codigo': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control'
                }),
            'qtd_minima': forms.NumberInput(attrs={
                'class': 'form-control'
                }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
        
        labels = {
            'nome': 'Nome',
            'codigo': 'Código',
            'descricao': 'Descrição',
            'qtd_minima': 'Quantidade Mínima'
        }
        
        help_texts = {
            'foto': 'Formatos aceitos: JPG, PNG, GIF (máx. 5MB)'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].required = True
        self.fields['nome'].max_length = 200
        
    
        

