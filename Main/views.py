from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, VentaForm, BuscarClienteForm
from .models import Cliente, Producto

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main:lista_clientes')  # Redirigir a la lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'Main/agregar_cliente.html', {'form': form})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main:lista_productos')  # Redirigir a la lista de productos
    else:
        form = ProductoForm()
    return render(request, 'Main/agregar_producto.html', {'form': form})


def buscar_cliente(request):
    if request.method == 'GET':
        form = BuscarClienteForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clientes = Cliente.objects.filter(nombre__icontains=nombre)
        else:
            clientes = Cliente.objects.all()
    else:
        form = BuscarClienteForm()
        clientes = Cliente.objects.all()

    return render(request, 'Main/buscar_cliente.html', {'form': form, 'clientes': clientes})


# views.py
from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()  # Trae todos los clientes desde la base de datos
    return render(request, 'Main/lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'Main/lista_productos.html', {'productos': productos})

def lobby(request):
    return render(request, 'Main/lobby.html')

