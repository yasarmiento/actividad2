from django import forms
from apps.usuario.models import Ventas

class Ventasform(forms.ModelForm):
    class Meta:
	
        model = Ventas
    
        fields = {
                'fecha',
                'valortotal',
                'tipopago',
                'usuarioid',
                'vehiculo',
        }