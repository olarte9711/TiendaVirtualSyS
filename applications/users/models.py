from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
#
#from .managers import UserManager

class User(AbstractBaseUser):
    # TIPO DE USUARIOS
    ADMINISTRADOR = '0'
    ARTISTA = '1'
    # GENEROS
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'
    #
    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ARTISTA, 'Artista'),
    ]

    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    email = models.EmailField(unique=True)
    full_name = models.CharField('Nombres', max_length=100)
    ocupacion = models.CharField(
        max_length=1, 
        choices=OCUPATION_CHOICES, 
        blank=True
    )
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
    def __str__(self):
        """Unicode representation of Estampa."""
        return str(self.id)+'-'+self.full_name  +'-' +self.ocupacion