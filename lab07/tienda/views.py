from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import Http404
from .models import Categoria, Producto
from tienda.carrito import Cart
# Create your views here.
def index(request):
    product_list=Producto.objects.order_by('nombre')[:6]
    category_list=Categoria.objects.order_by('nombre')
    context = {'product_list':product_list,'category_list':category_list}
    return render(request,'index.html', context)

def producto(request,producto_id):
    producto=get_object_or_404(Producto,pk=producto_id)
    category_list=Categoria.objects.order_by('nombre')
    return render (request, 'producto.html', {'producto':producto,'category_list':category_list})

def categoria(request,categoria_nombre):
    categoria_obj=get_object_or_404(Categoria,nombre=categoria_nombre)
    product_list=get_list_or_404(Producto,categoria=categoria_obj)
    category_list=Categoria.objects.order_by('nombre')
    return render (request, 'listproductos.html', {'product_list':product_list,'category_list':category_list})


#acciones de ShopCart
def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
    