from apps.APUs.api.serializer.general_serializer import MaterialRelationSerializers, APUsSerializers
from apps.APUs.models import AnalysisOfUnitaryPricesModel

from rest_framework import generics, status
from rest_framework.response import Response

"""Vista para modificar las relaciones de los materiales"""
class MaterialRelListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MaterialRelationSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    """Modificacion del metodo get para enviar todos los materiales por APU"""
    def get(self, request):
        apu = AnalysisOfUnitaryPricesModel.objects.all()
        apu_serializer = APUsSerializers(apu, many = True).data

        for apu in apu_serializer:
            material = self.get_serializer().Meta.model.objects.filter(id_APU = apu['id'])
            apu['material'] = MaterialRelationSerializers(material, many=True).data

        return Response(apu_serializer)

    def post(self, request):
        serializer = self.serializer_class(sata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Elemento agregado al APU'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

