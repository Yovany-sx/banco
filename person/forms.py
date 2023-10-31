from base.models import Municipality, Parish, State
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Person


class PersonForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre
    first_name = forms.CharField(
        label=_('Nombres:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-toggle': 'tooltip',
                'title': _('Ingrese su nombre/s'),
            }
        )
    )

    # Apellido
    last_name = forms.CharField(
        label=_('Apellidos:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-toggle': 'tooltip',
                'title': _('Ingrese su apellido/s'),
            }
        )
    )

    # Cédula de identidad
    identification_card = forms.CharField(
        label=_('DPI:'),
        max_length=13,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Número de DPI',
                'data-toggle': 'tooltip',
                'title': _('Ingrese su número de DPI'),
            }
        ),
        help_text=_('Ingrese su número de DPI sin espacion ni guiones')
    )

    # Número telefónico
    phone = forms.CharField(
        label=_('Teléfono:'),
        max_length=8,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Número de teléfono', 
                'data-toggle': 'tooltip',
                'title': _('Ingrese su número de teléfono'),
            }
        ),
        help_text=_('(país)-área-número')
    )

    # Correo Electrónico
    email = forms.EmailField(
        label=_('Correo Electrónico:'),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-sm email-mask',
                'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip',
                'title': _('Indique el correo electrónico de contacto con el\
                 usuario')
            }
        )
    )

    # Departamento
    state = forms.ModelChoiceField(
        label=_('Departamento:'), queryset=State.objects.all(),
        empty_label=_('Seleccione...'),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2',
            'data-toggle': 'tooltip',
            'title': _('Seleccione el departamento donde se encuentra ubicado'),
            'onchange': "combo_update(\
                this.value, 'base', 'Municipality', 'state', 'pk', 'name',\
                'id_municipality')",
        })
    )

    # Municipio
    municipality = forms.ModelChoiceField(
        label=_('Municipio:'), queryset=Municipality.objects.all(),
        empty_label=_('Seleccione...'),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2',
            'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _('Seleccione el municipio donde se encuentra ubicada'),
            'onchange': "combo_update(this.value, 'base', 'Parish',\
            'municipality', 'pk', 'name', 'id_parish')",
        })
    )

    # Parroquia
    parish = forms.ModelChoiceField(
        label=_('Cantón/Aldea:'), queryset=Parish.objects.all(),
        empty_label=_('Seleccione...'),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm select2',
            'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _('Seleccione el Cantón o Aldea donde se encuentra ubicada'),
        })
    )

    # Dirección
    address = forms.CharField(
        label=_('Dirección:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-toggle': 'tooltip',
                'title': _('Indique la dirección exacta'),
            }
        )
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        model = Person
        exclude = ['user']
