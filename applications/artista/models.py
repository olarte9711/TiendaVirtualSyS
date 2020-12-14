from django.db import models

class Artista(models.Model):
    """Model definition for Artista."""

    # TODO: Define fields here
    nombres = models.CharField('Nombre', max_length=30)
    apellidos = models.CharField('Apellidos', max_length=30)
    email = models.CharField('E-mail', max_length=50)
    username = models.CharField("Username", max_length=50)
    password = models.CharField("Contraseña", max_length=50)


    class Meta:
        """Meta definition for Artista."""

        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        """Unicode representation of Artista."""
        return str(self.id)+'-'+self.nombres+'-'+self.apellidos

