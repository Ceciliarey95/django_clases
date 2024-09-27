from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=20, null=False)
    autor = models.CharField(max_length=20, null= False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True,upload_to='libros', default='libros/libro_default.png')

    def __str__(self):
        return self.titulo