from django.db import models
from apps.base.models import SuppliesBaseModel, RelationshipBaseModel

"""Modelo para las familias de los materiales"""
class MaterialsFamilyModel(models.Model):

    id = models.AutoField(primary_key= True)
    description = models.CharField('Descripción', max_length=20)

    class Meta:
        verbose_name = ("Familia de material")
        verbose_name_plural = ("Familias de materiales")

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

    class Meta:
        verbose_name = ("Familia de herramienta")
        verbose_name_plural = ("Familias de herramientas")
        
    def __str__(self):
        return self.description
    
"""Modelo para las herramientas"""
class ToolsModel(SuppliesBaseModel):

    id_family = models.ForeignKey(ToolsFamilyModel, verbose_name='Familia de herramientas', on_delete=models.CASCADE, blank=True)
    brand = models.CharField('Marca', max_length=50, null=True, blank=True)
    class Meta:
        verbose_name = ("Herramienta")
        verbose_name_plural = ("Herramientas")
    def __str__(self):
        return self.description

"""Modelo para mano de obra"""
class LabourModel(SuppliesBaseModel):
    
    fact_real_salary = models.DecimalField('Factor de salario real', max_digits=5, decimal_places=2, default=1)
    is_real_salary = models.BooleanField('Aplica factor de salario real?', default=False)
    
    class Meta:
        verbose_name = ("Mano de obra")
        verbose_name_plural = ("Mano de obra")

    class Meta:
        verbose_name = ("Mano de obra")
        verbose_name_plural = ("Mano de obra")

    def __str__(self):
        return self.description

"""Modelo para subcontratos a todo costo"""
class SubcontractJobModel(SuppliesBaseModel):
    
    class Meta:
        verbose_name = ("Subcontrato")
        verbose_name_plural = ("Subcontratos")
    def __str__(self):
        return self.description
    
"""Modelo para fletes"""
class FreightModel(SuppliesBaseModel):

    class Meta:
        verbose_name = ("Flete")
        verbose_name_plural = ("Fletes")

    def __str__(self):
        return self.description
    
"""Modelo para equipos"""
class EquipmentModel(SuppliesBaseModel):

    class Meta:

        verbose_name = ("Equipos")
        verbose_name_plural = ("Equipos")


    def __str__(self):
        return self.description
    
"""Modelo para equipos auxiliares"""
class AuxEquipmentModel(SuppliesBaseModel):

    class Meta:
        verbose_name = ("Equipo auxiliar")
        verbose_name_plural = ("Equipos auxiliares")
    def __str__(self):
        return self.description