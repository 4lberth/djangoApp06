# Generated by Django 5.1.1 on 2024-10-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_categoria_imagen_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]
