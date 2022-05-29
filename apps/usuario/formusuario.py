from django import forms
from apps.usuario.models import Usuario

class Usuarioform(forms.ModelForm):
    class Meta:
	
        model = Usuario
    
        fields = {
                'nombre',
                'correo',
                'telefono',
                'direccion',
        }