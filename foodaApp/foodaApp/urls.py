from django.contrib import admin
from django.urls import path
from meususuarios.views import UserList
from produtos.views import ProductList
from categorias.views import CategoryList
from pedidos.views import NovoPedido
from pedidos.views import MercadoPagoTokenView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', CategoryList.as_view(), name='category-list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('produtos/', ProductList.as_view(), name='product-list'),
    path('novo_pedido/', NovoPedido.as_view(), name='novo_pedido'),
    path('pagamento_mp/', MercadoPagoTokenView.as_view(), name='pagamento_mp')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
