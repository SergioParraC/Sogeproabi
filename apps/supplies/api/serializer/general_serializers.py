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
            'journalist': instance.cost,
            'data_aditional': instance.data_aditional,
            'factor_real_salary': instance.fact_real_salary,
            'is_real_salary': instance.is_real_salary
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
        }