from django import forms
from person.models import Person, Donacion, Grupo_sanguineo
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class DonacionForm(forms.ModelForm):
    
    donante = forms.ModelChoiceField(queryset=Person.objects.all(), label='Donante:', empty_label='Seleccione un donante')
    quantity = forms.FloatField(label='Cantidad:' , required=True, widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-toggle': 'tooltip',
                'title': _('Ingrese la cantidad de mililitros donados'),
            }))
    date = forms.DateField(label='Fecha:')
    grupo_sanguineo = forms.ModelChoiceField(queryset=Grupo_sanguineo.objects.all(), label='Grupo Sanguíneo:', empty_label='Seleccione grupo sanguíneo')
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise ValidationError(_('La cantidad no puede ser negativa.'))
        if quantity == 0:
            raise ValidationError(_('La cantidad no puede ser cero.'))
        return quantity

    date = forms.DateField(label='Fecha:')
    grupo_sanguineo = forms.ModelChoiceField(queryset=Grupo_sanguineo.objects.all(), label='Grupo Sanguíneo:', empty_label='Seleccione grupo sanguíneo')
                                             
    class Meta:
        model = Donacion
        exclude = ['user']
        fields = ['donante', 'quantity', 'date', 'grupo_sanguineo']
