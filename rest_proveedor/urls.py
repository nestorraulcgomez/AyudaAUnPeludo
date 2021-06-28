from django.urls import path
from rest_proveedor.views import lista_proveedores,agregar_proveedor,detalle_proveedor
from rest_proveedor.viewsLogin import login

urlpatterns = [
    path('proveedores',lista_proveedores,name="proveedores"),
    path('agregar-proveedor',agregar_proveedor,name="agregar_proveedor"),
    path('proveedor/<id>',detalle_proveedor, name="detalle_proveedor"),
    path('login',login, name="login"),
]