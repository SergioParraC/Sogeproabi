from apps.supplies.api.serializer.general_serializers import MaterialSerializer, LabourSerializer
from apps.supplies.api.views.general_views import GeneralListCreateAPIView, GeneralRetrieveUpdateDestroyAPIView

"""Listar y crear los materiales"""
class MaterialListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = MaterialSerializer

"""Editar y eliminar los materiales"""
class MaterialRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer

"""Listar y crear la mano de obra"""
class LabourListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = LabourSerializer

"""Editar y eliminar la mano de obra"""
class LabourRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = LabourSerializer