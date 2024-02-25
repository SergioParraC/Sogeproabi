from apps.APUs.api.serializer.general_serializer import *
from apps.APUs.models import AnalysisOfUnitaryPricesModel

from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import F

"""Vista generica para listar y añadir las relaciones de los insumos"""
class GeneralRelListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = None

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    """Modificacion del metodo get para enviar todos los insumos por APU"""
    def get(self, request, item):
        apu = AnalysisOfUnitaryPricesModel.objects.filter(key_user_item=item)
        apu_serializer = APUsSerializers(apu, many = True).data
        
        """Se realiza un bucle para concatenar la info del material al APU"""
        sum_total_price = 0
        for apu in apu_serializer:

            material = self.get_serializer().Meta.model.objects.filter(id_APU = apu['id'])

            #Obtiene el valor del precio total del insumo
            price = self.get_serializer().Meta.model.objects.filter(id_APU = apu['id'], ).annotate(total_price =  F('cost') * F('cant'))
            
            for item in price:
                sum_total_price = sum_total_price + item.total_price

            
            apu['material'] = self.serializer_class(material, many=True).data

        apu_serializer.append({'total_price': sum_total_price})
        return Response(apu_serializer)

    """Modificacipin de post"""
    def post(self, request, item = None):
        print(request.data)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Elemento agregado al APU'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""Vista generica para detallar, actualizar y eliminar insumos"""
class GeneralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = None
    loop_dield = "id"

    def get_queryset(self):
        apu = AnalysisOfUnitaryPricesModel.objects.filter(key_user_item=self.kwargs["item"]).values('id')
        print(apu)
        #Extrae el item que se está modificando, evia ingresar a otros apus que no tiene nada que ver
        for elemt in apu:
            id_elemet = elemt['id']
        #Filtra por el APU pasado por la url
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs["pk"]).filter(id_APU = id_elemet)
    
    def patch(self, request, pk = None):
        if self.get_queryset(pk):
            element_serializer = self.serializer_class(self.get_queryset(id=self.kwargs['pk']))
            return Response(element_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe elemento buscado'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            element_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if element_serializer.is_valid():
                element_serializer.save()
                return Response(element_serializer.data, status=status.HTTP_200_OK)
            return Response(element_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        element = self.get_queryset().filter(id = pk).first()
        if element:
            element.state = False
            element.save()
            return Response({'message': 'Elemento eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un elemento con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

"""Vista de APUs general"""
class GeneralAPUsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = APUsListSerializer
    def get_queryset(self):
        return AnalysisOfUnitaryPricesModel.objects.all()
    
    def get(self, request):
        apu_model = AnalysisOfUnitaryPricesModel.objects.all()
        apu_serializer = APUsListSerializer(apu_model, many =True).data
        return Response(apu_serializer)
    
    """Modificacion de post"""
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'APU agregado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""Listado de APUs"""
class APURetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = APUsListSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs['pk'])
    
    def patch(self, request, item = None):
        if self.get_queryset():
            element_serializer = self.serializer_class(self.get_queryset())
            return Response(element_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe APU buscado'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset():
            element_serializer = self.serializer_class(self.get_queryset(), data = request.data)
            if element_serializer.is_valid():
                element_serializer.save()
                return Response(element_serializer.data, status=status.HTTP_200_OK)
            return Response(element_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        element = self.get_queryset().first()
        if element:
            element.delete()
            return Response({'message': 'APU eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe el APU con estos datos'}, status = status.HTTP_400_BAD_REQUEST)