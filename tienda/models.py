from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria_id = models.CharField(max_length=50)  # Corrected to categoria_id
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        unique_together = ('nombre', 'categoria_id')  # Corrected to categoria_id
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} el {self.fecha_pedido}"

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    imagen = models.ImageField(upload_to='comentarios_imagenes/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)  # Esto guarda la fecha y hora actual cuando se crea el comentario

    def __str__(self):
        return f"{self.nombre} - {self.comentario[:30]}"

