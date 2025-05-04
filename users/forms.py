from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    """
    A custom form for creating new users with additional fields and styling.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    
    terms = forms.BooleanField(
        required=True,
        error_messages={'required': 'Você deve aceitar os termos de uso para criar uma conta.'}
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adding styling to default fields
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome de usuário'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar senha'})
        
        # Custom error messages
        self.fields['username'].error_messages = {
            'unique': _('Este nome de usuário já está em uso. Por favor, escolha outro.'),
            'required': _('O nome de usuário é obrigatório.'),
        }
        
        # Password validation messages
        self.fields['password1'].error_messages = {
            'required': _('É necessário definir uma senha.'),
        }
        self.fields['password2'].error_messages = {
            'required': _('Por favor, confirme sua senha.'),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Este e-mail já está em uso. Por favor, use outro endereço de e-mail.'))
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form with improved styling and error messages.
    """
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
        error_messages={
            'required': _('Por favor, digite seu nome de usuário.'),
        }
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        error_messages={
            'required': _('Por favor, digite sua senha.'),
        }
    )
    
    error_messages = {
        'invalid_login': _(
            "Nome de usuário ou senha incorretos. Por favor, verifique seus dados e tente novamente."
        ),
        'inactive': _("Esta conta está inativa. Entre em contato com o administrador."),
    }