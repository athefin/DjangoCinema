from django.contrib import admin
from mainApp.models import Pelicula, Funcion, Ventas

# Register your models here.
class PeliculaForm(admin.ModelAdmin):
    list_dispaly=['nombre', 'anno', 'director']

class FuncionForm(admin.ModelAdmin):
    list_display=['pelicula', 'fecha', 'hora', 'asientos_vendidos', 'sala']

class VentasForm(admin.ModelAdmin):
    list_display=['funcion', 'cliente', 'entradas', 'total_original', 'total_final']

admin.site.register(Pelicula, PeliculaForm)
admin.site.register(Funcion, FuncionForm)
admin.site.register(Ventas, VentasForm)
