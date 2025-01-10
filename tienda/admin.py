from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido

# Registro y personalización del modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('id',)

# Registro y personalización del modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria_id')  # Corrected to categoria_id
    search_fields = ('nombre', 'categoria_id')  # Corrected to categoria_id


# Registro y personalización del modelo Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')
    ordering = ('id',)

# Registro y personalización del modelo Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_pedido', 'total')
    list_filter = ('fecha_pedido',)
    search_fields = ('cliente__nombre', 'productos__nombre')
    ordering = ('-fecha_pedido',)
    filter_horizontal = ('productos',)


