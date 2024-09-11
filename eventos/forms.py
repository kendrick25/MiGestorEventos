from django import forms
from .models import Evento, Organizador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'organizador']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if 'Cancelado' in nombre:
            raise forms.ValidationError('El nombre no se puede cancelar.')
        return nombre
class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe este correo electrónico.')
        return email