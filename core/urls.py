from django.urls import path
from .views import index, listar_proveedores, contacto, formularioE, seccionGatos, seccionPerros, form_mod_proveedor, nuevo_proveedor, eliminar_proveedor

urlpatterns=[
    path('', index, name="index"),
    path('inicio/', index, name="inicio"),
    path('listar-proveedores/', listar_proveedores, name="listar_proveedores"),
    path('contacto/', contacto, name="contacto"),
    path('formulario-enviado/', formularioE, name="formulario-enviado"),
    path('seccion-gatos/', seccionGatos, name="seccion-gatos"),
    path('seccion-perros/', seccionPerros, name="seccion-perros"),
    path('modificar_proveedor/<id>', form_mod_proveedor, name='modificar_proveedor'),
    path('nuevo_proveedor/', nuevo_proveedor, name='nuevo_proveedor'),
    path('eliminar_proveedor/<id>', eliminar_proveedor, name='eliminar_proveedor'),
    
]