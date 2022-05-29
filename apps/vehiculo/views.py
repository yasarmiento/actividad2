from django.shortcuts import render, redirect
from apps.vehiculo.formtipovehiculo import Tipovehiculoform
from apps.vehiculo.formvehiculo import Vehiculoform
from apps.vehiculo.models import Vehiculo, Tipovehiculo

def inicio(request):    
    vehiculo = Vehiculo.objects.all().order_by('id')
    return render(request,'paginas/vehiculo.html', {'vehiculo': vehiculo})

def create(request):
    if request.method == 'POST':
        form = Vehiculoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = Vehiculoform()
        return render(request,'paginas/vehiculoform.html', {'form': form})

def update(request,id):
    vehiculo = Vehiculo.objects.get(id=id)
    if request.method == 'GET':
        form = Vehiculoform(instance=vehiculo)
    else:
        form = Vehiculoform(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    return render(request, 'paginas/vehiculoform.html', {'form': form})

def delete(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect('inicio')


def iniciotv(request):    
    tipovehiculo = Tipovehiculo.objects.all().order_by('id')
    return render(request,'paginas/tipovehiculo.html', {'tipovehiculo': tipovehiculo})

def createtv(request):
    if request.method == 'POST':
        form = Tipovehiculoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tvinicio')
    else:
        form = Tipovehiculoform()
        return render(request,'paginas/tipovehiculoform.html', {'form': form})

def updatetv(request,id):
    tipovehiculo = Tipovehiculo.objects.get(id=id)
    if request.method == 'GET':
        form = Tipovehiculoform(instance=tipovehiculo)
    else:
        form = Tipovehiculoform(request.POST, instance=tipovehiculo)
        if form.is_valid():
            form.save()
            return redirect('tvinicio')
    return render(request, 'paginas/tipovehiculoform.html', {'form': form})

def deletetv(request, id):
    tipovehiculo = Tipovehiculo.objects.get(id=id)
    tipovehiculo.delete()
    return redirect('tvinicio')