
# python
from datetime import timedelta
# django
from django.utils import timezone
from django.db import models
#
from applications.producto.models import Camiseta
from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper


class CarShopManager(models.Manager):
    """ procedimiento modelo Carrito de compras """
    
    def total_cobrar(self):
        
        consulta = self.aggregate(
            total=Sum(
                F('camiseta__valor'),
                output_field=FloatField()
            ),
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0 

class SaleManager(models.Manager):
    """ procedimiento para modelo venta """
    
    
    def total_ventas_dia(self):
        consulta = self.filter(
            close=False,
            anulate=False
        ).aggregate(
            total=Sum('amount')
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0
    
    def total_ventas_anuladas_dia(self):
        consulta = self.filter(
            close=False,
            anulate=True
        ).aggregate(
            total=Sum('amount')
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0
    
    def total_ventas(self):
        return self.filter(
            anulate=False,
        ).aggregate(
            total=Sum('amount')
        )['total']
    
    def ventas_en_fechas(self, date_start, date_end):
        return self.filter(
            anulate=False,
            date_sale__range=(date_start, date_end),
        ).order_by('-date_sale')

class SaleDetailManager(models.Manager):
    """ procedimiento modelo product """
    
    def detalle_por_venta(self, id_venta):
        return self.filter(
            sale__id=id_venta
        )

    def ventas_mes_producto(self, id_prod):
        # creamos rango de fecha
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30)
        
        consulta = self.filter(
            sale__anulate=False,
            created__range=(start_date, end_date),
            product__pk=id_prod,
        ).values('sale__date_sale__date', 'product__name').annotate(
            cantidad_vendida=Sum('count'),
        )
        return consulta
    
    def restablecer_stok_num_ventas(self, id_venta):
        prods_en_anulados = []
        for venta_detail in self.filter(sale__id=id_venta):
            #actualizmso producot
            venta_detail.product.count = venta_detail.product.count + venta_detail.count
            venta_detail.product.num_sale = venta_detail.product.num_sale - venta_detail.count
            prods_en_anulados.append(venta_detail.product)
        Product.objects.bulk_update(prods_en_anulados, ['count', 'num_sale'])
        return True
    
    def resumen_ventas(self):
        return self.filter(
            sale__anulate=False,
            sale__close=True,
        ).values('sale__date_sale__date').annotate(
            total_vendido=Sum(
                F('price_sale')*F('count'),
                output_field=FloatField()
            ),
            total_ganancias=Sum(
                F('price_sale')*F('count') - F('price_purchase')*F('count'),
                output_field=FloatField()
            ),
            num_ventas=Sum('count'),
        )
    
  
    