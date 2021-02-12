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
    DeleteView
)
from .models import Estampa

from .forms import EstampaForm

class ListAllEstampa(ListView):
    template_name = 'producto/lista_catalogo.html'
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

class EstampaUpdateView(UpdateView):
    model = Estampa
    template_name = "producto/update.html"
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
    template_name = "producto/delete.html"
    success_url = reverse_lazy('estampa_app:correcto')