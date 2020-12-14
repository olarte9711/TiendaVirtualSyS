from django.db import models
from applications.artista.models import Artista


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
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Estampa."""

        verbose_name = 'Estampa'
        verbose_name_plural = 'Estampas'

    def __str__(self):
        """Unicode representation of Estampa."""
        return str(self.id)+'-'+self.nombre

