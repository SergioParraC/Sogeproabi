from django.db import models
from apps.base.models import SuppliesBaseModel, RelationshipBaseModel
from django.contrib.auth.models import User

"""Modelo para las familias de los materiales"""
class MaterialsFamilyModel(models.Model):

    id = models.AutoField(primary_key= True)
    description = models.CharField('Descripción', max_length=20)

    def __str__(self):
        return self.description

"""Modelo para materiales"""
class MaterialsModel(SuppliesBaseModel):
    id_family = models.ForeignKey(MaterialsFamilyModel, verbose_name="Familia del mateiral", on_delete=models.CASCADE)
    brand = models.CharField('Marca', max_length=50, blank=True)

    class Meta:
        verbose_name = ("Material")
        verbose_name_plural = ("Materiales")

    def __str__(self):
        return self.description

"""Modelo para las familias de las herramientas"""
class ToolsFamilyModel(models.Model):

    id = models.AutoField(primary_key= True)
    description = models.CharField('Descripción', max_length=20, null=False, blank=False)

    def __str__(self):
        return self.description
    
"""Modelo para las herramientas"""
class ToolsModel(SuppliesBaseModel):

    id_family = models.ForeignKey(ToolsFamilyModel, verbose_name='Familia de herramientas', on_delete=models.CASCADE, blank=True)
    brand = models.CharField('Marca', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.description

"""Modelo para mano de obra"""
class LabourModel(SuppliesBaseModel):
    
    fact_real_salary = models.DecimalField('Factor de salario real', max_digits=5, decimal_places=5, default=1)
    is_real_salary = models.BooleanField('Aplica factor de salario real?', default=False)

"""Modelo para subcontratos a todo costo"""
class SubcontractJobModel(SuppliesBaseModel):
    
    def __str__(self):
        return self.description
    
"""Modelo para fletes"""
class FreightModel(SuppliesBaseModel):

    def __str__(self):
        return self.description
    
"""Modelo para equipos"""
class EquipmentModel(SuppliesBaseModel):

    def __str__(self):
        return self.description
    
"""Modelo para equipos auxiliares"""
class AuxEquipmentModel(SuppliesBaseModel):

    def __str__(self):
        return self.description