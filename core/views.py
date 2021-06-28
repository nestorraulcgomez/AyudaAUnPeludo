from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.
def index(request):

    return render(request, 'core/index.html')

def proveedores(request):

    proveedores = Proveedor.objects.all()

    contexto = {
        'proveedores' : proveedores

    }
    
    return render(request, 'core/proveedores.html',contexto)

def contacto(request):
    
    return render(request, 'core/contacto.html')

def seccionGatos(request):
    
    return render(request, 'core/seccion-gatos.html')

def seccionPerros(request):
    
    return render(request, 'core/seccion-perros.html')

def formularioE(request):
    
    return render(request, 'core/formulario-enviado.html')

def nuevo_proveedor (request):
    datos = {
        'form' : ProveedorForm()
    }
    if request.method=='POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado Correctamente"
        else:
            datos['mensaje']="Cambios no guardados"  
    return render(request, 'core/nuevo_proveedor.html', datos)

def form_mod_proveedor (request,id):
    proveedor =get_object_or_404(Proveedor,rut = id)
    datos = {
        'form' : ProveedorForm(instance=proveedor)
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST,instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificados correctamente" 
            datos['form'] = formulario
        else:
           datos['mensaje']="Los cambios no han sido modificados"  
    return render(request, 'core/form_mod_proveedor.html', datos)

def eliminar_proveedor (request,id):
    proveedor = get_object_or_404(Proveedor,rut = id)
    proveedor.delete()

    return redirect(to='proveedores')