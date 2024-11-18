from django.urls import path
from . import views
from .views import CategoriaListCreate, CategoriaDetail, ProductoListCreate, ProductoDetail, ProductosPorCategoria

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('categoria/<int:categoria_id>/productos/', ProductosPorCategoria.as_view(), name='productos-por-categoria'),  # Asegúrate de que esta línea esté presente
    path('categoria/', CategoriaListCreate.as_view(), name='categoria-list-create'),
    path('producto/', ProductoListCreate.as_view(), name='producto-list-create'),
]



