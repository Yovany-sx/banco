from base.models import Parish
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """!
    Clase que contiene las personas

  
    """

    # Nombre
    first_name = models.CharField('nombres', max_length=100)

    # Apellido
    last_name = models.CharField('apellidos', max_length=100)

    # Cédula de identidad
    identification_card = models.CharField(
        'dpi',
        max_length=13,
        # validators=[
        #     validators.RegexValidator(
        #         r'^[VE][\d]{8}$',
        #         _('Introduzca un número de cédula válido. Solo se permiten\
        #         números y una longitud de 8 carácteres. Se agrega un 0 si la \
        #         longitud es de 7 carácteres.')
        #     ),
        # ], unique=True
    )

    # Número telefónico
    phone = models.CharField(
        'teléfono',
        max_length=8,
        # validators=[
        #     validators.RegexValidator(
        #         r'd{4}-\d{4}$',
        #         _('Número telefónico inválido. Solo se permiten números.')
        #     ),
        # ]
    )

    # Correo electrónico
    email = models.CharField(
        'correo electrónico', max_length=100, help_text=('correo@correo.com')
    )

    # Dirección
    address = models.CharField('dirección', max_length=100)

    # Relación entre la persona y la parroquia
    parish = models.ForeignKey(
        Parish, on_delete=models.CASCADE, verbose_name='Cantón/Aldea'
    )

    # Relación entre la persona y el usuario del sistema
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='usuario'
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre, apellido y la
            cédula de identidad
        """

        return '%s %s' % (
            self.first_name, self.last_name
        )

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = _('Donante')
        verbose_name_plural = _('Donantes')

class Factor(models.Model):  # +    - 
    factor = models.CharField(max_length=10)
    
    def __str__(self):
        return self.factor
    
    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        """

        verbose_name = _('Factor')
        verbose_name_plural = _('Factores')
    
class Grupo_sanguineo(models.Model): # A -
    tipo = models.CharField(max_length=150)
    factor=models.ForeignKey(Factor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.tipo} {self.factor}"
    
    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        """

        verbose_name = _('Grupo')
        verbose_name_plural = _('Grupos Sanguineos')

class Donacion(models.Model):
    quantity=models.FloatField('cantidad')
    date=models.DateField('fecha_donacion',auto_now_add=False)
    donante=models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    grupo_sanguineo=models.ForeignKey(Grupo_sanguineo, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s, %s, %s, %s' % (self.donante, self.grupo_sanguineo, self.quantity, self.date)
    
    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        """

        verbose_name = _('Donacion')
        verbose_name_plural = _('Donaciones')