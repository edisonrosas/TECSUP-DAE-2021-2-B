from django.contrib import admin
from tienda.models import Categoria,Producto,Cliente
from django.contrib import admin 
# Register your models here.
admin.site.register(Categoria)
class ProductoAdmin(admin.ModelAdmin):
    list_display={'nombre'}

admin.site.register(Producto)
admin.site.register(Cliente)

