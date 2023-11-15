from apps.supplies.models import *

from rest_framework import serializers

"""Serializador de los materiales"""
class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialsModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'brand': instance.brand,
            'family_description': instance.id_family.description,
            'user_create': instance.id_user_create.username
        }

"""Serializador de mano de obra"""
class LabourSerializer(serializers.ModelSerializer):

    class Meta:
        model = LabourModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'factor_real_salary': instance.fact_real_salary,
            'is_real_salary': instance.is_real_salary,
            'user_create': instance.id_user_create.username
        }
        
"""Serializador de las herramientas"""
class ToolsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToolsModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'brand': instance.brand,
            'family_description': instance.id_family.description,
            'user_create': instance.id_user_create.username
        }
        
"""Serializador de los subcontratos"""
class SubcontractJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubcontractJobModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'user_create': instance.id_user_create.username
        }
        
"""Serializador de los fletes"""
class FreightSerializer(serializers.ModelSerializer):

    class Meta:
        model = FreightModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'user_create': instance.id_user_create.username
        }
        
"""Serializador de los equipos"""
class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'user_create': instance.id_user_create.username
        }
        
        
"""Serializador de los equipos"""
class AuxEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuxEquipmentModel
        exclude = ('id',)

    def to_representation(self, instance):
        return{
            'description': instance.description,
            'unit': instance.unit,
            'data_aditional': instance.data_aditional,
            'user_create': instance.id_user_create.username
        }