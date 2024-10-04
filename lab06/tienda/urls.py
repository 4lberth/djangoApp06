#from django.urls import path
from . import views
#

app_name = 'tienda'

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('producto/<int:producto_id>/', views.producto, name='producto'),
#    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),  # Nueva ruta para productos por categoría
#]
from django.urls import path
from .views import CategoriaListCreate, CategoriaDetail, ProductoListCreate, ProductoDetail

urlpatterns = [
    path('categoria/', CategoriaListCreate.as_view(), name='categoria-list-create'),
    path('categoria/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('producto/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('producto/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
]
