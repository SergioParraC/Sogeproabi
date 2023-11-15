from apps.APUs.models import *
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
                #'family_description': instance.id_family.id_materials.id_family.description,
            }
        }

"""Vista para añadir las herramientas"""
class ToolsRelationSerializers(serializers.ModelSerializer):

    class Meta:
        model = ToolsRelarionshipModel
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'unit_cost': instance.cost,
            'total_cost': instance.cost * instance.cant,
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'tools': {
                'description': instance.id_tool.description,
                'unit': instance.id_tool.unit,
                'data_aditional': instance.id_tool.data_aditional,
                'brand': instance.id_tool.brand,
            }
        }
        
"""Vista para añadir subcontratos"""
class SubRelationSerializers(serializers.ModelSerializer):

    class Meta:
        model = SubcontractJobRelarionshipModel
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'unit_cost': instance.cost,
            'total_cost': instance.cost * instance.cant,
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'subcontract': {
                'description': instance.id_subcontract.description,
                'unit': instance.id_subcontract.unit,
                'data_aditional': instance.id_subcontract.data_aditional,
            }
        }

"""Vista para añadir fletes"""
class FreightRelationSerializers(serializers.ModelSerializer):

    class Meta:
        model = FreightRelarionshipModel
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'unit_cost': instance.cost,
            'total_cost': instance.cost * instance.cant,
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'freight': {
                'description': instance.id_freight.description,
                'unit': instance.id_freight.unit,
            }
        }

"""Vista para añadir equipos"""
class EquipmentRelationSerializers(serializers.ModelSerializer):

    class Meta:
        model = EquipmentRelarionshipModel
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'unit_cost': instance.cost,
            'total_cost': instance.cost * instance.cant,
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'equipment': {
                'description': instance.id_equipment.description,
                'unit': instance.id_equipment.unit,
                'data_aditional': instance.id_equipment.data_aditional,
            }
        }
        
"""Vista para añadir equipos auxiliares"""
class AuxEquipmentRelationSerializers(serializers.ModelSerializer):

    class Meta:
        model = AuxEquipmentRelarionshipModel
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id_user_create': instance.id_user_create.username,
            'cant': instance.cant,
            'unit_cost': instance.cost,
            'total_cost': instance.cost * instance.cant,
            'date_create': instance.date_create,
            'date_edit': instance.date_edit,
            'aux_equipment': {
                'description': instance.id_equipment.description,
                'unit': instance.id_equipment.unit,
                'data_aditional': instance.id_equipment.data_aditional,
            }
        }

"""Serializer basico para listar los APUs"""
class APUsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnalysisOfUnitaryPricesModel
        fields = '__all__'
        
    def to_representation(self, instance):
        return{
            'id': instance.id,
            'key': instance.key_user_item,
            'description': instance.description,
            'unit': instance.unit,
            'user_create': instance.id_user_create.username
        }