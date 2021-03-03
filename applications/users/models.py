from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
#
from .managers import UserManager

class User(AbstractBaseUser):
    # TIPO DE USUARIOS
    ADMINISTRADOR = '0'
    ARTISTA = '1'
    CLIENTE = '2'
    # GENEROS
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'
    #
    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ARTISTA, 'Artista'),
        (CLIENTE,'Cliente'),
    ]

    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    username  = models.CharField( max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank = True)
    apellidos = models.CharField( max_length=30, blank = True)
    full_name = models.CharField( max_length=30, blank = True)
    ocupation = models.CharField(
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
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    
    def __str__(self):
        """Unicode representation of Estampa."""
        return str(self.id)+'-'+self.nombres  +'-' +self.ocupation