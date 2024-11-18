from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria
from rest_framework import generics
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductoSerializer

# Vistas para la tabla Categoria
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vistas para la tabla Producto
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



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


class ProductosPorCategoria(APIView):
    def get(self, request, categoria_id):
        # Verificar si la categoría existe
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        
        # Filtrar productos por la categoría
        productos = Producto.objects.filter(categoria=categoria)
        serializer = ProductoSerializer(productos, many=True)
        
        # Devolver los productos como respuesta JSON
        return Response(serializer.data)