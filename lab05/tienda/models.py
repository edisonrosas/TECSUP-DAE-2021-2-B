from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(default=0)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    nombres=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200)
    dni=models.PositiveIntegerField()
    telefono=models.CharField(max_length=15)
    direccion=models.TextField()
    email=models.EmailField(max_length=254)
    born_date=models.DateTimeField('date birth')
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.nombres