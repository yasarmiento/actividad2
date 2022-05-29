from django.shortcuts import render,redirect
from apps.usuario.models import Usuario, Ventas, Vehiculoventas
from apps.usuario.formusuario import Usuarioform
from apps.usuario.formventas import Ventasform
from apps.usuario.formvehiculosventas import Vehiculosventasform


# Create your views here.

def uinicio(request):    
    usuario = Usuario.objects.all().order_by('id')
    return render(request,'paginas/usuario.html', {'usuario': usuario})

def ucreate(request):
    if request.method == 'POST':
        form = Usuarioform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uinicio')
    else:
        form = Usuarioform()
        return render(request,'paginas/usuarioform.html', {'form': form})

def uupdate(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'GET':
        form = Usuarioform(instance=usuario)
    else:
        form = Usuarioform(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('uinicio')
    return render(request, 'paginas/usuarioform.html', {'form': form})

def udelete(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('uinicio')

def ventinicio(request):    
    ventas = Ventas.objects.all().order_by('id')
    return render(request,'paginas/ventas.html', {'ventas': ventas})

def ventcreate(request):
    if request.method == 'POST':
        form = Ventasform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventinicio')
    else:
        form = Ventasform()
        return render(request,'paginas/ventasform.html', {'form': form})

def ventupdate(request,id):
    ventas = Ventas.objects.get(id=id)
    if request.method == 'GET':
        form = Ventasform(instance=ventas)
    else:
        form = Ventasform(request.POST, instance=ventas)
        if form.is_valid():
            form.save()
            return redirect('ventinicio')
    return render(request, 'paginas/ventasform.html', {'form': form})

def ventdelete(request, id):
    ventas = Ventas.objects.get(id=id)
    ventas.delete()
    return redirect('uinicio')

def vehinicio(request):    
    vehiculoventas = Vehiculoventas.objects.all().order_by('id')
    return render(request,'paginas/vehiculosventas.html', {'vehiculoventas': vehiculoventas})

def vehcreate(request):
    if request.method == 'POST':
        form = Vehiculosventasform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehinicio')
    else:
        form = Vehiculosventasform()
        return render(request,'paginas/vehiculosventasform.html', {'form': form})

def vehupdate(request,id):
    vehiculoventas = Vehiculoventas.objects.get(id=id)
    if request.method == 'GET':
        form = Vehiculosventasform(instance=vehiculoventas)
    else:
        form = Vehiculosventasform(request.POST, instance=vehiculoventas)
        if form.is_valid():
            form.save()
            return redirect('vehinicio')
    return render(request, 'paginas/vehiculosventasform.html', {'form': form})

def vehdelete(request, id):
    vehiculoventas = Vehiculoventas.objects.get(id=id)
    vehiculoventas.delete()
    return redirect('vehinicio')