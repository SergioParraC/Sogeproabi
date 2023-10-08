from django.db import models
from django.contrib.auth.models import User

"""Modelo base para crear todos los insumos"""
class SuppliesBaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    description = models.TextField('Descripción', null=False, blank=False)
    unit = models.CharField('Unidad de media', max_length=15, null=False, blank=False)
    data_aditional = models.CharField('Datos adicionales', max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = ("Modelo base para insumo")
        verbose_name_plural = ("Modelo base para insumos")

"""Modelo base para relaciones"""
class RelationshipBaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_user_item = models.CharField("Código", max_length=15, blank=False, null=False)
    id_user_create = models.ForeignKey(User, verbose_name="Id usuario que creo el insumo", on_delete=models.CASCADE)
    cant = models.IntegerField("Cantidad", blank=False, null=False)
    cost = models.DecimalField('Costo total', max_digits=8, decimal_places=2, blank=False)
    date_create = models.DateTimeField("Fecha y hora de creación", auto_now=False, auto_now_add=True)
    date_edit = models.DateTimeField("Fecha y hora de modificación", auto_now=True, auto_now_add=False)
    date_delete = models.DateTimeField('Fecha y hora de eliminación', auto_now=True, auto_now_add=False)
    state = models.BooleanField('Estado', default=True)

    class Meta:
        abstract = True
        verbose_name = ("Modelo base de relación")
        verbose_name_plural = ("Modelo base de relaciones")
