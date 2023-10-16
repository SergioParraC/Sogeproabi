from apps.APUs.api.serializer.general_serializer import MaterialRelationSerializers
from apps.APUs.api.views.general_views import GeneralRelListCreateAPIView, GeneralRetrieveUpdateDestroyAPIView

"""Vista para mostrar los materiales"""
class MaterialRelListCreateAPIView(GeneralRelListCreateAPIView):
    serializer_class = MaterialRelationSerializers

class MaterialsRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = MaterialRelationSerializers

"""Vista para mostrar mano de obra"""