from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventoList, name='lista_eventos'),
    path('crearE/', views.crear_evento, name='crear_evento'),
    path('organizadores/', views.organizadoresList.as_view(), name='organizadores'),
    path('organizadores/crear', views.CrearOrganizador.as_view(), name='organizadorForm'),
    path('editar/<int:pk>/', views.eventoEditar, name='editar_evento'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('registro/', views.register, name='registro'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
]