 # django
from django import forms
# local
from .models import Estampa, Camiseta


class EstampaForm(forms.ModelForm):
    
    class Meta:
        model = Estampa
        fields = (
            'id',
            'nombre',
            'descripcion',
            'valor',
            'tema',
            'popularidad',
            'imagen',
            'artista',
            'stock',
            'num_ventas',
        )
        widgets = {
            'id': forms.TextInput(
                attrs = {
                    'placeholder': 'ID',
                    'class': 'input-group-field',
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombre de estampa',
                    'class': 'input-group-field',
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'placeholder': 'Descripcion del producto',
                    'rows': '3',
                    'class': 'input-group-field',
                }
            ),
            'valor': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),
            
        }

class CamisetaForm(forms.ModelForm):
    class Meta:
        model = Camiseta
        fields = (
            'num_documento',
            'talla',
            'color',
            'material',
        )
        widgets = {
            'nom_comprador': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombre de estampa',
                    'class': 'input-group-field',
                }
            ),
        }
    # validations
   
    
    
    
  