
from django import forms
from .models import Cliente, Producto, Venta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'direccion', 'telefono']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'fecha_venta', 'cantidad']


class BuscarClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    

