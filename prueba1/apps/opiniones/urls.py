from django.urls import path
from .views import agregar_opinion, ModificarOpinion, EliminarOpinion

app_name = 'apps.opiniones'

urlpatterns = [
    path('agregar_opinion/', agregar_opinion, name='agregar_opinion'),
    path('modificar_opinion/<int:pk>', ModificarOpinion.as_view(), name = 'modificar_opinion' ),
    path('eliminar_opinion/<int:pk>', EliminarOpinion.as_view(), name = 'eliminar_opinion' )
]