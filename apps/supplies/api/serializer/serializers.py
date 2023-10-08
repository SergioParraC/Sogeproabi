from apps.supplies.models import (
    MaterialsModel, MaterialsFamilyModel,ToolsFamilyModel, LabourModel, SubcontractJobModel, FreightModel, EquipmentModel, AuxEquipmentModel
)
from rest_framework import serializers

"""Serializador de los materiales"""
class MaterialSerializers(serializers.ModelSerializer):

    class Meta:
        model = MaterialsModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'family_description': instance.id_family.description,
            'brand': instance.brand
        }
    
