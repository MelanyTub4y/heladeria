from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos_view, name='productos'),
    path('sobrenosotras/', views.sobrenosotras, name='sobrenosotras'),
    path('clientes/', views.clientes, name='clientes'),
    path('pedido/', views.pedidos, name='pedido'),  # Cambiar de 'pedidos/' a 'pedido/'
    path('categorias/', views.categorias, name='categorias'),  # Make sure this is correct
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

