from django.db import models
from django.conf import settings
from django.db.models.signals import pre_delete, post_save
#
from model_utils.models import TimeStampedModel

# local apps
from applications.producto.models import Camiseta
from applications.venta.managers import CarShopManager, SaleManager, SaleDetailManager

#
#from .managers import SaleManager, SaleDetailManager, CarShopManager
#from .signals import update_stok_ventas_producto

class Sale(TimeStampedModel):
    """Modelo que representa a una Venta Global"""

    # tipo recibo constantes
    FACTURA = '1'
    SIN_COMPROBANTE = '2'
    # tipo pago constantes
    TARJETA = '0'
    CASH = '1'
    BONO = '2'
    OTRO = '3'
    #
    TIPO_INVOCE_CHOICES = [
        
        (FACTURA, 'Factura'),
        (SIN_COMPROBANTE, 'Sin Comprobante'),
    ]

    TIPO_PAYMENT_CHOICES = [
        (TARJETA, 'Tarjeta'),
        (CASH, 'Cash'),
        (BONO, 'Bono'),
        (OTRO, 'Otro'),
    ]

    date_sale = models.DateTimeField(
        'Fecha de Venta',
    )
    amount = models.DecimalField(
        'Monto', 
        max_digits=10, 
        decimal_places=2
    )
    type_invoce = models.CharField(
        'TIPO',
        max_length=2,
        choices=TIPO_INVOCE_CHOICES
    )
    type_payment = models.CharField(
        'TIPO PAGO',
        max_length=2,
        choices=TIPO_PAYMENT_CHOICES
    )
    anulate = models.BooleanField(
        'Venta Anulada',
        default=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='usuario',
        related_name="user_venta",
    )

    objects = SaleManager()

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'ventas'

    def __str__(self):
        return 'Nº [' + str(self.id) + '] - ' + str(self.date_sale)



class SaleDetail(TimeStampedModel):
    """Modelo que representa a una venta en detalle"""

    camiseta = models.ForeignKey(
        Camiseta,
        on_delete=models.CASCADE,
        verbose_name='camiseta',
        related_name='camiseta_sale'
    )
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE, 
        verbose_name='Codigo de Venta',
        related_name='detail_sale'
    )
    price_sale = models.DecimalField(
        'Precio Venta', 
        max_digits=10, 
        decimal_places=2
    )
    anulate = models.BooleanField(default=False)
    #

    objects = SaleDetailManager()

    class Meta:
        verbose_name = 'Producto Vendido'
        verbose_name_plural = 'Productos vendidos'

    def __str__(self):
        return str(self.sale.id) + ' - ' + str(self.camiseta.estampa.nombre)
class CarShop(TimeStampedModel):
    """Modelo que representa a un carrito de compras"""

    code = models.CharField(
        max_length=13,
        unique=True
    )
    camiseta = models.ForeignKey(
        Camiseta,
        on_delete=models.CASCADE,
        verbose_name='producto',
        related_name='product_car'
    )
    
    objects = CarShopManager()

    class Meta:
        verbose_name = 'Carrito de compras'
        verbose_name_plural = 'Carrito de compras'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)+'-'+ str(self.camiseta.estampa.nombre) +'-'+str(self.camiseta.num_documento)
