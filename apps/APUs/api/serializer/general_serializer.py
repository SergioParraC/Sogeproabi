from apps.APUs.models import (
    MaterialsRelationshipModel, AnalysisOfUnitaryPricesModel, LabourRelarionshipModel
)
from rest_framework import serializers

"""Vista general para los APUs"""
class APUsSerializers(serializers.ModelSerializer):#Ciudad
    class Meta:
        model = AnalysisOfUnitaryPricesModel

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'key': instance.key_user_item,
            'description': instance.description,
            'unit': instance.unit,
            'user_create': instance.id_user_create.username
        }

"""Vista para los materiales"""
class MaterialRelationSerializers(serializers.ModelSerializer):#Persona
    class Meta:
        model = MaterialsRelationshipModel
        exclude = ('id','state','date_delete')

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'unit_cost': instance.cost,
            'total_cost': instance.cost * instance.cant,
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'materials': {
                'description': instance.id_materials.description,
                'unit': instance.id_materials.unit,
                'data_aditional': instance.id_materials.data_aditional,
                'brand': instance.id_materials.brand,
                #'family_description': instance.id_family.id_materials.id_family.description,
            }
        }

"""Vista para la mano de obra"""
class LabourRelationSerializers(serializers.ModelSerializer):#Persona
    class Meta:
        model = LabourRelarionshipModel
        exclude = ('id','state','date_delete')

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'salary': instance.cost,
            'factor_real_salary': instance.id_labour.fact_real_salary,
            'is_real_salary': instance.id_labour.is_real_salary,
            'total_cost': instance.cost * instance.cant * (instance.id_labour.is_real_salary if instance.id_labour.fact_real_salary else 1),
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'materials': {
                'description': instance.id_labour.description,
                'unit': instance.id_labour.unit,
                'data_aditional': instance.id_labour.data_aditional,
                'brand': instance.id_labour.brand,
                #'family_description': instance.id_family.id_materials.id_family.description,
            }
        }