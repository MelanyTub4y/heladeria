from .forms import ComentarioForm
from .models import Comentario
from django.shortcuts import render, redirect
from .models import Producto

def home(request):
    return render(request, 'home.html')


def productos_view(request):
    # Si deseas aplicar algún filtro, puedes modificar esta línea
    productos = Producto.objects.all()  # Puedes agregar filtros si los necesitas, por ejemplo: .filter(categoria='helados')

    # Pasa los productos al contexto
    context = {
        'productos': productos,
    }

    # Devuelve la respuesta con el contexto
    return render(request, 'productos.html', context)

def clientes(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES)
        if form.is_valid():
            comentario = form.save()
            print(f"Nuevo comentario recibido: {comentario.nombre} - {comentario.comentario}")
            return redirect('clientes')  # Redirigir después de enviar
    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.all().order_by('-fecha')
    return render(request, 'clientes.html', {'form': form, 'comentarios': comentarios})

def categorias(request):
    return render(request, 'categorias.html')

def sobrenosotras(request):
    return render(request, 'sobrenosotras.html')

def pedidos(request):
    productos = Producto.objects.all()  # Obtén todos los productos de la base de datos
    return render(request, 'pedidos.html', {'productos': productos})  # Pasa los productos al template