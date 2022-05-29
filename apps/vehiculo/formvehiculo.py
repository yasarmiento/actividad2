from django import forms
from apps.vehiculo.models import Vehiculo

class Vehiculoform(forms.ModelForm):
    class Meta:
	
        model = Vehiculo
    
        fields = {
                'modelo',
                'color',
                'placa',
                'motor',
                'marcaid',
                'tipovehiculoid',
        }
