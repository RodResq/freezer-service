from django.contrib import admin
from django.urls import path, include
from gerencia.views import index
from django.conf import settings
from django.conf.urls.static import static
from gerencia.views import index

web_urlpatterns = [
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('locais-armazenamento/', include('local_armazenamento.urls', namespace='local_armazenamento')),
    path('categorias/', include('categoria_peca.urls', namespace='categorias_peca')),
    path('pecas', include('peca.urls', namespace='peca'))
]

api_urlpatterns = [
    path('api/', include('setup.api_urls')),
]

admin_urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = admin_urlpatterns + web_urlpatterns + api_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
