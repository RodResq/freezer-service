from django import forms
from categoria_peca.models import CategoriaPeca
from local_armazenamento.models import LocalArmazenamento
from fornecedor.models import Fornecedor
from .models import Peca


class PecaForm(forms.ModelForm):
    
    class Meta:
        model = Peca
        fields = ['nome', 'codigo', 'descricao', 'qtd_minima', 'qtd_estoque', 'unidade', 'valor', 
                 'id_categoria_peca', 'id_local_armazenamento', 'id_fornecedor', 'foto']
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
            'qtd_estoque': forms.NumberInput(attrs={
                'class': 'form-control'
                }),
            'unidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: UN, KG, M, L'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': 0
            }),
            'id_categoria_peca': forms.Select(attrs={
               'class': 'form-select' 
            }),
            'id_local_armazenamento': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_fornecedor': forms.Select(attrs={
                'class': 'form-select'
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
            'qtd_minima': 'Quantidade Mínima do estoque',
            'qtd_estoque': 'Quantidade Estoque Entrada',
            'unidade': 'Unidade de Medida',
            'valor': 'Valor Unitário (R$)',
            'id_categoria_peca': 'Categoria',
            'id_local_armazenamento': 'Local de Armazenamento',
            'id_fornecedor': 'Fornecedor',
            'foto': 'Foto da Peça'
        }
        
        help_texts = {
            'foto': 'Formatos aceitos: JPG, PNG, GIF (máx. 5MB)',
            'unidade': 'Ex: UN (unidade), KG (quilograma), M (metro), L (litro)',
            'valor': 'Valor unitário da peça em reais'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].required = True
        self.fields['codigo'].required = False
        self.fields['descricao'].required = True
        self.fields['id_categoria_peca'].required = True
        
        self.fields['id_categoria_peca'].queryset = CategoriaPeca.objects.all().order_by('nome')
        self.fields['id_categoria_peca'].empty_label = 'Selecione uma categoria'
        
        self.fields['id_local_armazenamento'].queryset = LocalArmazenamento.objects.all().order_by('setor', 'estante', 'prateleira');
        self.fields['id_local_armazenamento'].empty_label = 'Selecione um local (opcional)'
        
        self.fields['id_fornecedor'].queryset = Fornecedor.objects.all().order_by('nome')
        self.fields['id_fornecedor'].empty_label = "Selecione um fornecedor (opcional)"
        
        if not self.instance.pk:
            self.fields['qtd_minima'].initial = 0
            self.fields['qtd_estoque'].initial = 0
        
        
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if codigo:
            codigo = codigo.strip().upper()
            existe_peca = Peca.objects.filter(codigo__iexact=codigo)
            if self.instance.pk:
                existe_peca = existe_peca.exclude(pk=self.instance.pk)
            if existe_peca.exists():
                raise forms.ValidationError('Já existe uma peça com este código.')
        
        return codigo
        
        
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome:
            nome = nome.strip().title()
        return nome
        
        
    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor is not None and valor < 0:
            raise forms.ValidationError('O valor não pode ser negativo.')
        return valor
        
        
    def clean_qtd_minima(self):
        qtd = self.cleaned_data.get('qtd_minima')
        if qtd is not None and qtd < 0:
            raise forms.ValidationError('A quantidade mínima não pode ser negativa.')
        return qtd
    
    def clean_qtd_estoque(self):
        qtd_estoque = self.cleaned_data.get('qtd_estoque')
        if qtd_estoque is not None and qtd_estoque < 0:
            raise forms.ValidationError('A quantidade estoque não pode ser negativa.')
        return qtd_estoque

