from django.urls import path, include
from estoque import views

api_v1_patterns = [
    path('estoque/', include('estoque.api_urls')),
    # path('fornecedor/', include('fornecedor.api_urls'), name='fornecedor'),
]

urlpatterns = [
    path('v1/', include(api_v1_patterns)),
    # path('v2/', include(api_v2_patterns)),
]