from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView
)

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    
    # Password reset URLs
    path('password-reset/', 
         CustomPasswordResetView.as_view(), 
         name='password_reset'),
    
    path('password-reset/done/', 
         CustomPasswordResetDoneView.as_view(), 
         name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
         CustomPasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
    
    path('password-reset-complete/', 
         CustomPasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
]