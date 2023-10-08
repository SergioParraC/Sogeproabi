from apps.supplies.api.serializer.general_serializers import MaterialSerializer
from apps.supplies.api.views.general_views import GeneralListCreateAPIView, GeneralRetrieveUpdateDestroyAPIView

class MaterialListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = MaterialSerializer

class MaterialRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer
