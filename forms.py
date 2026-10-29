from django import forms
from mainApp.models import Funcion



class FormVentas(forms.Form):
    LARGO_CODIGO=9
    VALIDADOR_CODIGO=37
    id_funcion=forms.CharField(widget=forms.HiddenInput)
    cliente=forms.CharField()
    email=forms.CharField(required=False)
    entradas=forms.IntegerField(min_value=1,max_value=10)
    codigo=forms.CharField(required=False)


    id_funcion.widget.attrs['class']='from-control'
    cliente.widget.attrs['class']='form-control'
    email.widget.attrs['class']='form-control'
    entradas.widget.attrs['class']='form-control'
    codigo.widget.attrs['class']='form-control'

def clean_entradas(self):
    id_funcion=self.cleaned_data['id_funcion']
    entradas=self.cleaned_data['entradas']

    funcion=Funcion.objects.get(id=id_funcion)
    entradas_disponibles=funcion.asientos_disponibles


def clean_cofigo(self):
    codigo=self.cleaned__data['codigo']
    if codigo=="" : return codigo

    codigoErroneo=False
    if (len(codigo)!=self.LARGO_CODIGO): codigoErroneo=True
    if not codigo.isnumeric(): codigoErroneo=True


    suma=0 
    for c in codigo:
        suma +=int(c)

        if suma!=self.VALIDADOR_CODIGO : codigoErroneo=True

        if (codigoErroneo):
            raise forms.ValidationError("Codigo incorrecto")

        return codigo