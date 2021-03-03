from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class EstampaManager(models.Manager):
    """ procedimiento modelo product """
    
    def filtrar(self, **filters):
        
        consulta = self.filter(
            Q(nombre__icontains=filters['kword'])
        ).filter(
            artista__full_name__icontains=filters['artista'],
            
        ).filter(
            popularidad__icontains=filters['popularidad'],
            tema__icontains=filters['tema'],
        )

        return consulta.order_by('nombre')
        