from django import forms

from .models import *

class VentasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'


    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'subtotal': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%','readonly': True}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%'}),
            'total': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%','readonly': True}),

        }