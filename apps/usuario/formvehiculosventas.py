from django import forms
from apps.usuario.models import Vehiculoventas

class Vehiculosventasform(forms.ModelForm):
    class Meta:
	
        model = Vehiculoventas
    
        fields = {
                'ventasid',
                'vehiculoid',
        }