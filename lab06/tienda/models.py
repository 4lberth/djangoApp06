from django.db import models
from django.core.validators import MinValueValidator


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pub_date = models.DateTimeField('fecha de registro', auto_now=True)
    imagen = models.URLField(max_length=200, blank=True, null=True)  # Cambiado a URLField

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0.01)])
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    imagen = models.URLField(max_length=200, blank=True, null=True)  # Cambiado a URLField

    def __str__(self):
        return self.nombre

