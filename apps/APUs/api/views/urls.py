from django.urls import path

from apps.APUs.api.views.specific_views import *
from apps.APUs.api.views.general_views import *



urlpatterns = [
    path('material/add/<str:item>', MaterialRelListCreateAPIView.as_view(), name = 'add_materials'),
    path('material/edit/<str:item>/<int:pk>', MaterialsRelRetrieveUpdateDestroyAPIView.as_view(), name='edit_materials'),
    path('labour/add/<str:item>', LabourRelListCreateAPIView.as_view(), name = 'add_labour'),
    path('labour/edit/<str:item>/<int:pk>', LabourRelRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_labour'),
    path('tools/add/<str:item>', ToolsListCreateAPIView.as_view(), name = 'add_tools'),
    path('tools/edit/<str:item>/<int:pk>', ToolsRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_tools'),
    path('sub/add/<str:item>', SubListCreateAPIView.as_view(), name = 'add_sub'),
    path('sub/edit/<str:item>/<int:pk>', SubRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_sub'),
    path('freight/add/<str:item>', FreightListCreateAPIView.as_view(), name = 'add_freight'),
    path('freight/edit/<str:item>/<int:pk>', FreightRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_freight'),
    path('equipment/add/<str:item>', EquipmentListCreateAPIView.as_view(), name = 'add_equipment'),
    path('equipment/edit/<str:item>/<int:pk>', EquipmentRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_equipment'),
    path('auxequipment/add/<str:item>', AuxEquipmentListCreateAPIView.as_view(), name = 'add_aux_equipment'),
    path('auxequipment/edit/<str:item>/<int:pk>', AuxEquipmentRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_aux_equipment'),
    path('add/', GeneralAPUsListCreateAPIView.as_view(), name = 'apu_list'),
    path('edit/<int:pk>', APURetrieveUpdateDestroyAPIView.as_view(), name = 'apu_edit')
]
