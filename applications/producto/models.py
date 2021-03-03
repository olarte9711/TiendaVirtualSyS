from django.db import models
from applications.users.models import User
from .managers import EstampaManager
from model_utils.models import TimeStampedModel
# Create your models here.
class Estampa(models.Model):
    """Model definition for Estampa."""
    TEMA_CHOICES={
        ('0','DEPORTE'),
        ('1','ARTE'),
        ('2','MUSICA'),
        ('3','TECNOLOGIA'),
        ('4','PELICULAS'),
        ('5','OTRO'),
    }
    POPULARIDAD_CHOICES={
        ('0','BAJA'),
        ('1','MEDIA'),
        ('2','ALTA'),
    }    

    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.TextField()
    valor = models.IntegerField()
    tema= models.CharField('TEMA', max_length=1,choices=TEMA_CHOICES)
    popularidad = models.CharField('Popularidad', max_length=1,choices=POPULARIDAD_CHOICES)
    imagen= models.ImageField(upload_to='producto', blank=True, null=True)
    artista = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.IntegerField()
    num_ventas = models.IntegerField()
    descontino = models.BooleanField(default="False")
    objects = EstampaManager()

    class Meta:
        """Meta definition for Estampa."""

        verbose_name = 'Estampa'
        verbose_name_plural = 'Estampas'

    def __str__(self):
        """Unicode representation of Estampa."""
        return str(self.id)+'-'+self.nombre

class Camiseta(models.Model):
    TALLA_CHOICES={
        ('0','S'),
        ('1','M'),
        ('2','L'),
        ('3','XL'),
    }
    COLOR_CHOICES={
        ('0','AZUL'),
        ('1','ROJO'),
        ('2','BLANCO'),
        ('3','NEGRO'),
        ('4','VERDE'),
        ('5','AMARILLO'),
    }
    MATERIAL_CHOICES={
        ('0','ALGODON'),
        ('1','POLIESTER'),
        ('2','TRI-BLEND'),
    }


    num_documento = models.CharField("Comprador", max_length=50)
    valor = models.IntegerField()
    estampa = models.ForeignKey(Estampa, on_delete=models.CASCADE)
    
    comprado = models.BooleanField(default="False")
    talla = models.CharField('Talla', max_length=1,choices=TALLA_CHOICES)
    color = models.CharField('Color', max_length=1,choices=COLOR_CHOICES)
    material = models.CharField('Material', max_length=1,choices=MATERIAL_CHOICES)
    class Meta:
        """Meta definition for Estampa."""

        verbose_name = 'Camiseta'
        verbose_name_plural = 'Camisetas'

    def __str__(self):
        """Unicode representation of Estampa."""
        return str(self.id)+'-'+self.estampa.nombre+'-'+self.num_documento