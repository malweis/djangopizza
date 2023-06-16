from django.shortcuts import render, redirect
from .models import Pizza, Ingrediente

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza_list.html', {'pizzas': pizzas})

def pizza_detail(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    return render(request, 'pizza_detail.html', {'pizza': pizza})

def pizza_create(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        activo = request.POST.get('activo', False)
        pizza = Pizza.objects.create(nombre=nombre, precio=precio, activo=activo)
        return redirect('pizzeria:pizza_detail', pk=pizza.pk)
    return render(request, 'pizza_create.html')

def ingrediente_list(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente_list.html', {'ingredientes': ingredientes})

def ingrediente_detail(request, pk):
    ingrediente = Ingrediente.objects.get(pk=pk)
    return render(request, 'ingrediente_detail.html', {'ingrediente': ingrediente})

def ingrediente_create(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        ingrediente = Ingrediente.objects.create(nombre=nombre, categoria=categoria)
        return redirect('pizzeria:ingrediente_detail', pk=ingrediente.pk)
    return render(request, 'ingrediente_create.html')
