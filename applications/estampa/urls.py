from django.contrib import admin
from django.urls import path
from . import views

app_name= "estampa_app"

urlpatterns = [
    path(
        'catalogo-estampa/',
        views.ListAllEstampa.as_view(),
        name='catalogo_estampas'
    ),
    path(
        'nueva-estampa/',
        views.EstampaCreateView.as_view(),
        name='nueva_estampa'
    ),
    path(
        'success/',
        views.Success.as_view(),
        name='correcto'
    ),
    path(
        'update-estampa/<pk>/',
        views.EstampaUpdateView.as_view(),
        name='modificar_estampa'),
    path(
        'delete-estampa/<pk>/',
        views.EstampaDeleteView.as_view(),
        name='eliminar_estampa'),
    
]