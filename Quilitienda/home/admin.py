from django.contrib import admin
from .models import Comprador, Categoria, Producto, Administrador, Pedido, Envio

admin.site.register(Comprador)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Administrador)
admin.site.register(Pedido)
admin.site.register(Envio)