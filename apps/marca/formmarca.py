from django import forms
from apps.marca.models import Marca

class Marcaform(forms.ModelForm):
    class Meta:
	
        model = Marca
    
        fields = {
                'nombre',
        }