from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Estampa

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio"""
    template_name='inicio.html'


class ListAllEstampa(ListView):
    template_name = 'estampa/lista_catalogo.html'
    ordering='first_name'
    context_object_name='estampas'
    def get_queryset(self):
        print('************************')
        palabra_clave = self.request.GET.get("kword",'')
         
        lista = Estampa.objects.filter(
            nombre__icontains = palabra_clave
        )
        return lista


class Success(TemplateView):
    template_name = "estampa/success.html"


class EstampaCreateView(CreateView):
    template_name = "estampa/add.html"
    model = Estampa
    fields = ('__all__')
    success_url = reverse_lazy('estampa_app:correcto')

class EstampaUpdateView(UpdateView):
    model = Estampa
    template_name = "estampa/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('estampa_app:correcto')

    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST['nombre'])
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        return  super(EstampaUpdateView, self).form_valid(form)

class EstampaDeleteView(DeleteView):
    model = Estampa
    template_name = "estampa/delete.html"
    success_url = reverse_lazy('estampa_app:correcto')
    
# Create your views here.
