from django.shortcuts import render

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
    FormView
)
from .models import Estampa, Camiseta
from applications.venta.models import CarShop

from .forms import EstampaForm, CamisetaForm
from django.db.models import Q, F

class ListAllEstampa(ListView):
    template_name = 'producto/lista_catalogo.html'
    context_object_name='estampas'
    #paginación
    paginate_by = 5
    ordering='nombre'

    def get_queryset(self):
        lista = Estampa.objects.filtrar(
            kword = self.request.GET.get("kword",''),
            artista=self.request.GET.get("artista",''),
            popularidad=self.request.GET.get("popularidad",''),
            tema=self.request.GET.get("tema",''),
        )
        return lista


class Success(TemplateView):
    template_name = "producto/success.html"


class Index(TemplateView):
    template_name = "home/base_home.html"


class EstampaDetailView(DetailView):
    model = Estampa
    template_name = "producto/detail_estampa.html"

    def get_context_data(self, **kwargs):
        context = super(EstampaDetailView, self).get_context_data(**kwargs)
        return context
    

class EstampaCreateView(CreateView):
    template_name = "producto/add.html"
    form_class = EstampaForm
    success_url = reverse_lazy('estampa_app:catalogo_estampas')
    

class AddCamiseta(FormView):
    template_name = "producto/add_camiseta.html"
    form_class = CamisetaForm
    success_url = reverse_lazy('venta_app:venta_index')

   

    def form_valid(self, form, *args, **kwargs):
        num_documento = form.cleaned_data['num_documento']
        talla = form.cleaned_data['talla']
        color = form.cleaned_data['color']
        material = form.cleaned_data['material']

        estampa = Estampa.objects.get(id=self.kwargs['pk'])
        valor_estampa = estampa.valor
        if material == '0':
            valor_estampa = int(valor_estampa) + 16000
        elif material=='1':
            valor_estampa = int(valor_estampa) + 12000
        else: valor_estampa = int(valor_estampa) + 10000


        camiseta = Camiseta.objects.create(
            num_documento = num_documento,
            talla = talla,
            color = color,
            material = material,
            comprado = False,
            valor = valor_estampa,
            estampa = estampa
        )
        
        CarShop.objects.create(
            code = camiseta.id,
            camiseta = camiseta
        )


       

        return super(AddCamiseta,self).form_valid(form)

class EstampaUpdateView(UpdateView):
    model = Estampa
    template_name = "producto/add.html"
    form_class = EstampaForm
    success_url = reverse_lazy('estampa_app:catalogo_estampas')


class EstampaDeleteView(DeleteView):
    model = Estampa
    template_name = "producto/delete.html"
    success_url = reverse_lazy('estampa_app:catalogo_estampas')