from django.urls import path

from .views import CrearRegistro, ActualizarRegistro, EliminarRegistro, mostrar_registros

app_name = 'apps.modulo1'

urlpatterns = [
    path('crear_registro/', CrearRegistro.as_view(), name= 'crear_registro'),
    path('actualiza_registro/<int:pk>', ActualizarRegistro.as_view(), name='actualizar_registro'),
    path('eliminar_registro/', EliminarRegistro.as_view(), name= 'eliminar_registro'),
    path('listar_registros/', mostrar_registros , name = 'mostrar_registros')
]