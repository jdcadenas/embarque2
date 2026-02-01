from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Embarque(models.Model):
    codigo_rastreo = models.CharField(max_length=100, unique=True)
    fecha_llegada = models.DateField()
    productos = models.ManyToManyField(Producto, related_name='embarques')

    def __str__(self):
        return self.codigo_rastreo