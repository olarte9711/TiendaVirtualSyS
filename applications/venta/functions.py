from django.utils import timezone
from django.db.models import Prefetch
#
from applications.producto.models import Camiseta, Estampa
#
from .models import Sale, SaleDetail, CarShop


def procesar_venta(self, **params_venta):
    # recupera la lista de productos en carrtio
    productos_en_car = CarShop.objects.all()
    if productos_en_car.count() > 0:
        
        # crea el objeto venta
        venta = Sale.objects.create(
            date_sale=timezone.now(),
            amount=0,
            type_invoce=params_venta['type_invoce'],
            type_payment=params_venta['type_payment'],
            user=params_venta['user'],
        )
        #
        ventas_detalle = []
        productos_en_venta = []
        for producto_car in productos_en_car:
            venta_detalle = SaleDetail(
                camiseta=producto_car.camiseta,
                sale=venta,
                price_sale=producto_car.camiseta.valor,
                
            )
            # actualizmos stok de producto en iteracion
            producto = producto_car.camiseta
            producto.estampa.num_ventas = producto.estampa.num_ventas + 1
            ventas_detalle.append(venta_detalle)
            productos_en_venta.append(producto)
            #
            venta.amount = venta.amount + producto_car.camiseta.valor

        venta.save()
        SaleDetail.objects.bulk_create(ventas_detalle)
        # actualizamos el stok
        Camiseta.objects.bulk_update(productos_en_venta, ['estampa'])
        # completada la venta, eliminamos productos delc arrito
        productos_en_car.delete()
        return venta
    else:
        return None