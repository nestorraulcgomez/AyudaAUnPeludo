from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request, 'core/index.html')

def listar_proveedores(request):

    proveedores = Proveedor.objects.all()

    contexto = {
        'proveedores' : proveedores

    }
    
    return render(request, 'core/listar_proveedores.html',contexto)

def contacto(request):
    
    return render(request, 'core/contacto.html')

def seccionGatos(request):
    
    return render(request, 'core/seccion-gatos.html')

def seccionPerros(request):
    
    return render(request, 'core/seccion-perros.html')

def formularioE(request):
    
    return render(request, 'core/formulario-enviado.html')

def nuevo_proveedor (request):
    data = {
        'form' : ProveedorForm()
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado Correctamente")
            return redirect(to="/listar-proveedores/")
        else:
            data["form"] = formulario
            data['mensaje']="Cambios no guardados"  
    return render(request, 'core/nuevo_proveedor.html', data)

def form_mod_proveedor (request,id):
    proveedor =get_object_or_404(Proveedor,rut = id)
    datos = {
        'form' : ProveedorForm(instance=proveedor)
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST,instance=proveedor,files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to="/listar-proveedores/")
        else:
           data["form"] = formulario  
    return render(request, 'core/form_mod_proveedor.html', datos)

def eliminar_proveedor(request,id):
    proveedor = get_object_or_404(Proveedor,rut = id)
    proveedor.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="listar_proveedores")