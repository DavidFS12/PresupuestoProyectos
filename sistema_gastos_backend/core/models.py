from django.db import models

class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)
    inversionistas = models.TextField()
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    numero_agua = models.CharField(max_length = 50)
    numero_luz = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Gastos(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, related_name='gastos')
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    proveedor = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.total}"
