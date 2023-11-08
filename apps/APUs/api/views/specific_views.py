from apps.APUs.api.serializer.general_serializer import MaterialRelationSerializers, LabourRelationSerializers
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