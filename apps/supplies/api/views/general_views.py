from apps.supplies.api.serializer.serializers import MaterialSerializers
from rest_framework import generics, status
from rest_framework.response import Response

class MaterialListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MaterialSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Material agregado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class MaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializers

    def get_queryset(self, pk = None):
        if (pk == None):
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def patch(self, pk = None):
        if self.get_queryset(pk):
            material_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(material_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe el elemento con esta información'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        material_serializer = self.serializer_class(self.get_queryset(pk), request.data)
        if material_serializer.is_valid():
            material_serializer.save()
            return Response(material_serializer.data, status = status.HTTP_200_OK)
        return Response(material_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk = None):
        material = self.get_queryset().filter(id = pk).first()
        if material:
            material.delete()
            return Response({'message': 'Elemento eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe elemento con estos datos'}, status = status.HTTP_400_BAD_REQUEST)