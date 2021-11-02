from django.contrib import admin
from .models import Categoria,Producto,Cliente
from django.contrib import admin 
# Register your models here.
admin.site.register(Categoria)
class ProductoAdmin(admin.ModelAdmin):
    list_display={'nombre'}

admin.site.register(Producto)
#admin.site.register(Cliente)
#class ProductoAdmin(admin.ModelAdmin):
#    list_display={'nombre'}#

#admin.site.register(Producto)
#admin.site.register(Noticia, NoticiaAdmin)
#class ProductoAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('titulo',),}

#class ProductoAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'nombre':nombre}
