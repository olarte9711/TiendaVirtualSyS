from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View
)
from .models import Sale, SaleDetail, CarShop
from .functions import procesar_venta

from applications.producto.models import Camiseta, Estampa


class AddCarView(ListView):
    template_name = 'venta/index.html'
    model= CarShop
    context_object_name= 'camisetas'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["camisetas"] = CarShop.objects.all()
        context["total_cobrar"] = CarShop.objects.total_cobrar()
        # formulario para venta con voucher
        #context['form_voucher'] = VentaVoucherForm
        return context
    
class CarShopDeleteView(DeleteView):
    model = CarShop
    success_url = reverse_lazy('venta_app:venta_index')

class CarShopDeleteAll(View):
    
    def post(self, request, *args, **kwargs):
        #
        CarShop.objects.all().delete()
        #
        return HttpResponseRedirect(
            reverse(
                'venta_app:venta_index'
            )
        )

class ProcesoVentaSimpleView( View):
    """ Procesa una venta simple """

    def post(self, request, *args, **kwargs):
        #
        procesar_venta(
            self=self,
            type_invoce=Sale.SIN_COMPROBANTE,
            type_payment=Sale.CASH,
            user=self.request.user,
        )
        #
        return HttpResponseRedirect(
            reverse(
                'venta_app:venta_index'
            )
        )
class SaleListView( ListView):
    template_name = 'venta/ventas.html'
    context_object_name = "ventas" 
    ordering = ['date_sale']

    def get_queryset(self):
        return Sale.objects.filter(anulate=False)

class SaleDeleteView( DeleteView):
    template_name = "venta/delete.html"
    model = Sale
    success_url = reverse_lazy('venta_app:venta_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.anulate = True
        self.object.save()
        success_url = self.get_success_url()

        return HttpResponseRedirect(success_url)