from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

def register_view(request):
    """
    Handle user registration
    """
    if request.user.is_authenticated:
        return redirect('index')  # Redirect to homepage if already logged in
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bem-vindo ao Sistema Antártida, {user.username}! Sua conta foi criada com sucesso.')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    """
    Handle user login
    """
    if request.user.is_authenticated:
        return redirect('')  # Redirect to homepage if already logged in
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next')
                if next_url and next_url != '':
                    return redirect(next_url)
                else:
                    return redirect('index')
                
                messages.success(request, f'Bem-vindo de volta, {user.username}!')
                return redirect(next_url)
        # If form is not valid, it will re-render the login page with form errors
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    """
    Handle user logout
    """
    logout(request)
    messages.info(request, 'Você foi desconectado.')
    return redirect('login')

@login_required
def profile_view(request):
    """
    Display user profile
    """
    return render(request, 'users/profile.html')

# Password Reset Views with custom templates
class CustomPasswordResetView(PasswordResetView):
    """
    Custom password reset view to use our themed template
    """
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    """
    Custom password reset done view
    """
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Custom password reset confirmation view
    """
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Custom password reset complete view
    """
    template_name = 'users/password_reset_complete.html'