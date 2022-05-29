from django import forms
from apps.vehiculo.models import Tipovehiculo

class Tipovehiculoform(forms.ModelForm):
    class Meta:
	
        model = Tipovehiculo
    
        fields = {
                'nombre',
        }