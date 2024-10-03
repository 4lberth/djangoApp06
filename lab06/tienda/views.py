from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria

# Vista principal con productos y categorías en el menú lateral
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]  # Lista de productos para la página principal
    categorias = Categoria.objects.all()  # Cargar todas las categorías
    context = {
        'product_list': product_list,
        'categorias': categorias,  # Incluir categorías en el contexto
    }
    return render(request, 'index.html', context)

# Vista de producto individual
def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()  # Cargar todas las categorías
    return render(request, 'producto.html', {'producto': producto, 'categorias': categorias})

# Vista para listar productos por categoría
def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()  # Cargar todas las categorías para el menú lateral
    context = {
        'categoria': categoria,
        'productos': productos,
        'categorias': categorias,  # Incluir categorías en el contexto
    }
    return render(request, 'productos_por_categoria.html', context)
