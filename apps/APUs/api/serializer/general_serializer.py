from apps.APUs.models import MaterialsRelationshipModel, AnalysisOfUnitaryPricesModel
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
            'cost': instance.cost,
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

