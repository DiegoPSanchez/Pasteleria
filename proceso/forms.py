from django import forms
from .models import Pedido

class nPedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ('imagen', 'fecha', 'tamaño', 'moldes', 'tipo', 'decoracion', 'cliente', 
                  'telefono', 'vendedor','precio',)
        widgets = {
            'fecha':forms.TextInput(attrs={'class': 'form-control'}),
            'tamaño':forms.TextInput(attrs={'class': 'form-control'}),
            'moldes':forms.TextInput(attrs={'class': 'form-control'}),
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'decoracion':forms.Textarea(attrs={'class': 'form-control'}),
            'cliente':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor':forms.TextInput(attrs={'class': 'form-control'}),
            'precio':forms.TextInput(attrs={'class': 'form-control'}),
            }



