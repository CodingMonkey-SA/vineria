from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
    name = models.CharField(max_length=50, default="N/A")
    productType = models.CharField(max_length=30, default="N/A")
    brand = models.CharField(max_length=30, default="N/A")
    price = models.FloatField(default='00.00')
    productStock = models.IntegerField(default='0')
    description = models.CharField(max_length=200, default="N/A")
    year = models.IntegerField(default='0000')
    variety = models.CharField(max_length=30, default="N/A")
    origin = models.CharField(max_length=30, default="N/A")
    maker = models.CharField(max_length=50, default="N/A")
    size = models.FloatField(default='00.00')
    codigo = models.CharField(primary_key=True,max_length=30, default="")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

class Venta(models.Model):
    products =  models.ManyToManyField(Product, through='VentaProducto')
    fecha = models.DateTimeField(auto_now=True)
    estado = models.TextField(max_length=2, default="BO")

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta)
    product = models.ForeignKey(Product)
    cant = models.IntegerField(default='0000')
    precio = models.FloatField(default='00.00')