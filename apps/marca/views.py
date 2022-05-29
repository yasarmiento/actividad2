from django.shortcuts import render,redirect
from apps.marca.formmarca import Marcaform
from apps.marca.models import Marca
# Create your views here.

def minicio(request):    
    marca = Marca.objects.all().order_by('id')
    return render(request,'paginas/marca.html', {'marca': marca})

def mcreate(request):
    if request.method == 'POST':
        form = Marcaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('minicio')
    else:
        form = Marcaform()
        return render(request,'paginas/marcaform.html', {'form': form})

def mupdate(request,id):
    marca = Marca.objects.get(id=id)
    if request.method == 'GET':
        form = Marcaform(instance=marca)
    else:
        form = Marcaform(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('minicio')
    return render(request, 'paginas/marcaform.html', {'form': form})

def mdelete(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect('minicio')