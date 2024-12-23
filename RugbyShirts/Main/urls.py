from django.urls import path
from . import views

app_name = 'Main' 

urlpatterns = [
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),  
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'), 
    path('lobby/', views.lobby, name='lobby'),
]

