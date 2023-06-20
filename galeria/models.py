from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms

class producto(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    creacion_fecha = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    correo = models.EmailField()
    clave = models.CharField(max_length=8)

    def __str__(self):
        return self.correo
    
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'clave']    
