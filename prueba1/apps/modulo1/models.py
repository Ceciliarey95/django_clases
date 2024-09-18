from django.db import models

# Create your models here.

class Modulo1(models.Model):
    nombre = models.CharField(max_length=20, null=False, unique=True)
    descripcion = models.TextField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering =('fecha_agregado',)