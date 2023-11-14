from apps.APUs.api.serializer.general_serializer import *
from apps.APUs.api.views.general_views import GeneralRelListCreateAPIView, GeneralRetrieveUpdateDestroyAPIView

"""Vista para mostrar los materiales"""
class MaterialRelListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = MaterialRelationSerializers

class MaterialsRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = MaterialRelationSerializers

"""Vista para mostrar mano de obra"""
class LabourRelListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = LabourRelationSerializers

class LabourRelRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = LabourRelationSerializers

"""Vista para mostrar mano de obra"""
class ToolsListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = ToolsRelationSerializers

class ToolsRetriebeUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = ToolsRelarionshipModel