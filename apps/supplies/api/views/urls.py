from django.urls import path
from apps.supplies.api.views.specific_views import *

urlpatterns = [
    path('material/add/', MaterialListCreateAPIView.as_view(), name = 'material_add'),
    path('material/edit/<int:pk>', MaterialRetrieveUpdateDestroyAPIView.as_view(), name = 'material_edit'),
    path('labour/add/', LabourListCreateAPIView.as_view(), name = 'labour_add'),
    path('labour/edit/<int:pk>', LabourRetrieveUpdateDestroyAPIView.as_view(), name = 'labour_edit'),
    path('tools/add/', ToolsListCreateAPIView.as_view(), name = 'labour_add'),
    path('tools/edit/<int:pk>', ToolsRetrieveUpdateDestroyAPIView.as_view(), name = 'labour_edit'),
    path('sub/add/', SubListCreateAPIView.as_view(), name = 'sub_add'),
    path('sub/edit/<int:pk>', SubRetrieveUpdateDestroyAPIView.as_view(), name = 'sub_edit'),
    path('freight/add/', FreightCreateAPIView.as_view(), name = 'freigth_add'),
    path('freight/edit/<int:pk>', FreightRetrieveUpdateDestroyAPIView.as_view(), name = 'freigth_edit'),
    path('equipment/add/', EquipmentCreateAPIView.as_view(), name = 'equipment_add'),
    path('equipment/edit/<int:pk>', EquipmentRetrieveUpdateDestroyAPIView.as_view(), name = 'equipment_edit'),
    path('auxequipment/add/', AusEquipmentCreateAPIView.as_view(), name = 'auxequipment_add'),
    path('auxequipment/edit/<int:pk>', AuxEquipmentRetrieveUpdateDestroyAPIView.as_view(), name = 'auxequipment_edit')
]
