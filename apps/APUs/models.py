from django.db import models
from apps.supplies.models import (
    MaterialsModel, ToolsModel, LabourModel, SubcontractJobModel, FreightModel, EquipmentModel, AuxEquipmentModel
)
from apps.base.models import RelationshipBaseModel
from django.contrib.auth.models import User

"""Modelo para generar los APUS"""
class AnalysisOfUnitaryPricesModel(models.Model):
    id = models.AutoField(primary_key = True)
    description = models.CharField('Descripción', max_length=500, blank=False)
    unit = models.CharField('Unidad de medida', max_length=15, blank=False)
    key_user_item = models.CharField('Código', max_length=15)
    id_user_create = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Analisis de Precios Unitarios APU")
        verbose_name_plural = ("Analisis de Precios Unitarios APU")

    def __str__(self):
        return f"{self.key_user_item}: {self.description}"

"""Tabla rompiendo relaciones muchos a muchos de materiales, se relaciona la base"""
class MaterialsRelationshipModel(RelationshipBaseModel):
    id_materials = models.ForeignKey(MaterialsModel, verbose_name="Material", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Relación de material - APU")
        verbose_name_plural = ("Relaciones de materiales - APU")
    
    def __str__(self):
        return f"{self.id_materials}: {self.cant}"

"""Tabla rompiendo relaciones muchos a muchos de mano de obra, se relaciona la base"""
class LabourRelarionshipModel(RelationshipBaseModel):
    id_labour = models.ForeignKey(LabourModel, verbose_name="Mano de obra", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Relación mano de obra - APU")
        verbose_name_plural = ("Relaciones mano de obra - APU")

    def __str__(self):
        return f"{self.id_labour}: {self.cant}"
    
"""Tabla rompiendo relaciones muchos a muchos de herramientas, se relaciona la base"""
class ToolsRelarionshipModel(RelationshipBaseModel):
    id_tool = models.ForeignKey(ToolsModel, verbose_name="Herramienta", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Relación herramientas - APU")
        verbose_name_plural = ("Relaciones herramientas - APU")
    def __str__(self):
        return f"{self.id_tool}: {self.cant}"
    
"""Tabla rompiendo relaciones muchos a muchos de subcontratos, se relaciona la base"""
class SubcontractJobRelarionshipModel(RelationshipBaseModel):
    id_subcontract = models.ForeignKey(SubcontractJobModel, verbose_name="Subcontrato", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Relación subcontratos - APU")
        verbose_name_plural = ("Relaciones subcontratos - APU")

    def __str__(self):
        return f"{self.id_subcontract}: {self.cant}"
    
"""Tabla rompiendo relaciones muchos a muchos de fletes, se relaciona la base"""
class FreightRelarionshipModel(RelationshipBaseModel):
    id_freight = models.ForeignKey(FreightModel, verbose_name="Subcontrato", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Relación fletes - APU")
        verbose_name_plural = ("Relaciones fletes - APU")

    def __str__(self):
        return f"{self.id_subcontract}: {self.cant}"
    
"""Tabla rompiendo relaciones muchos a muchos de equipos, se relaciona la base"""
class EquipmentRelarionshipModel(RelationshipBaseModel):
    id_equipment = models.ForeignKey(EquipmentModel, verbose_name="Subcontrato", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Relación equipos - APU")
        verbose_name_plural = ("Relaciones equipos - APU")

    def __str__(self):
        return f"{self.id_subcontract}: {self.cant}"

"""Tabla rompiendo relaciones muchos a muchos de equipos auxiliares, se relaciona la base"""
class AuxEquipmentRelarionshipModel(RelationshipBaseModel):
    id_equipment = models.ForeignKey(AuxEquipmentModel, verbose_name="Subcontrato", on_delete=models.CASCADE)
    id_APU = models.ForeignKey(AnalysisOfUnitaryPricesModel, verbose_name="APU", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Relación equipos auxiliares - APU")
        verbose_name_plural = ("Relaciones equipos auxiliares - APU")

    def __str__(self):
        return f"{self.id_subcontract}: {self.cant}"