
from django.contrib.admin.decorators import register
from tienda.models import Categoria,Producto,Cliente
from django.contrib import admin 
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)

