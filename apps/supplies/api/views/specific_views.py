from apps.supplies.api.serializer.general_serializers import *
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
    
"""Listar y crear la herramienta"""
class ToolsListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = ToolsSerializer

class ToolsRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = ToolsSerializer

"""Listar y crear subcontratos"""
class SubListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = SubcontractJobSerializer

class SubRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = SubcontractJobSerializer
    
"""Listar y crear Fletes"""
class FreightCreateAPIView(GeneralListCreateAPIView):
    serializer_class = FreightSerializer

class FreightRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = FreightSerializer
    
"""Listar y crear equipos"""
class EquipmentCreateAPIView(GeneralListCreateAPIView):
    serializer_class = EquipmentSerializer

class EquipmentRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = EquipmentSerializer
    
"""Listar y crear equipos auxiliares"""
class AusEquipmentCreateAPIView(GeneralListCreateAPIView):
    serializer_class = AuxEquipmentSerializer

class AuxEquipmentRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = AuxEquipmentSerializer