from apps.APUs.api.serializer.general_serializer import *
from apps.APUs.api.views.general_views import GeneralRelListCreateAPIView, GeneralRetrieveUpdateDestroyAPIView
from apps.APUs.models import AnalysisOfUnitaryPricesModel

from rest_framework import generics, status, viewsets
from rest_framework.response import Response

"""Vistar para listar los APUs"""
class APUsListCreateAPIView(generics.ListAPIView):
    serializer_class = AnalysisOfUnitaryPricesModel


"""Vista para mostrar los materiales"""
class MaterialRelListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = MaterialRelationSerializers

class MaterialsRelRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = MaterialRelationSerializers

"""Vista para mostrar mano de obra"""

class LabourRelListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = LabourRelationSerializers

class LabourRelRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = LabourRelationSerializers

"""Vista para mostrar herramienta"""
class ToolsListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = ToolsRelationSerializers

class ToolsRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = ToolsRelarionshipModel
    
"""Vista para mostrar subcontratos"""
class SubListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = SubRelationSerializers

class SubRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = SubRelationSerializers
    
"""Vista para mostrar fletes"""
class FreightListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = FreightRelationSerializers

class FreightRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = FreightRelationSerializers
    
"""Vista para mostrar equipos"""
class EquipmentListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = EquipmentRelationSerializers

class EquipmentRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = EquipmentRelationSerializers
    
"""Vista para mostrar equipos auxiliares"""
class AuxEquipmentListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = AuxEquipmentRelationSerializers

class AuxEquipmentRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = AuxEquipmentRelationSerializers

