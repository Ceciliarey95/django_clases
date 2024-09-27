from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import CrearCategoria, ActualizarCategoria, EliminarCategoria, CrearLibro, ActualizarLibro, ListarLibros, EliminarLibro

app_name = 'apps.libros'

urlpatterns = [
    path("agregar_categoria/", CrearCategoria.as_view(), name= 'agregar_categoria'),
    path("actualizar_categoria/<int:pk>", ActualizarCategoria.as_view(), name = 'actualizar_categoria'),
    path("eliminar_categoria/<int:pk>", EliminarCategoria.as_view(), name= 'eliminar_categoria'),
    path("agregar_libro/", CrearLibro.as_view(), name= 'agregar_libro'),
    path("actualizar_libro/<int:pk>", ActualizarLibro.as_view(), name = 'actualizar_libro'),
    path("eliminar_libro/<int:pk>", EliminarLibro.as_view(), name= 'eliminar_libro'),
    path("listar_libros/", ListarLibros.as_view(), name='listar_libros')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)