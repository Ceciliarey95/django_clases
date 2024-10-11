from django.db import models
from django.contrib.auth.models import User

from apps.libros.models import Libro

# Create your models here.
class Opinion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Opinion')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.texto
    
    class Meta:
        ordering = ['-fecha']