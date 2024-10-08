from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm, CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

def eventoList(request):
    eventos = Evento.objects.all()
    return render(request, 'evento.html', {'eventos': eventos})

@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    evento.delete()
    return redirect('lista_eventos')

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventoForm.html', {'form': form})

class organizadoresList(ListView):
    model = Organizador
    template_name = 'organizadores.html'
    context_object_name = 'organizadores'

class CrearOrganizador(LoginRequiredMixin, CreateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'organizadoresForm.html'
    success_url = reverse_lazy('organizadores')

@login_required
def eventoEditar(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventoEdit.html', {'form': form})

def iniciarSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_eventos')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciarSesion.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('iniciarSesion')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('index')
