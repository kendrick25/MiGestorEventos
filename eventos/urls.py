from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Eventos/', views.eventoList, name='lista_eventos'),
    path('CrearEventos/', views.crear_evento, name='crear_evento'),
    path('Organizadores/', views.organizadoresList.as_view(), name='organizadores'),
    path('Organizadores/crear', views.CrearOrganizador.as_view(), name='organizadorForm'),
    path('Editar/<int:pk>/', views.eventoEditar, name='editar_evento'),
    path('eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
    path('IniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('Registro/', views.register, name='registro'),
    path('CerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
]