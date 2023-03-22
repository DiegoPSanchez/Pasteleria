from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Pedido(models.Model):

    imagen = models.ImageField()
    fecha = models.DateTimeField()
    tamaño = models.CharField(max_length=200)
    moldes = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    decoracion = models.TextField()
    cliente = models.CharField(max_length=200)
    telefono = models.IntegerField()
    vendedor = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places = 2)
    registro = models.DateTimeField(auto_now=True)
    estado = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.fecha

    def toJSON(self):
        item = model_to_dict(self, exclude=['imagen', 'moldes', 'decoracion', 'telefono', 'vendedor','regitro', 'estado'])
        item['fecha'] = self.fecha.strftime('%d-%m-%Y %H:%M')
        item['tamaño'] = self.tamaño.toJSON()
        item['tipo'] = self.tipo.toJSON()
        item['cliente'] = self.cliente.toJSON()
        item['precio'] = format(self.precio, '.2f')
        return item
    