from django.urls import path
from apps.APUs.api.views.specific_views import *
from apps.APUs.api.views.general_views import *


urlpatterns = [
    path('material/add/<str:item>', MaterialRelListCreateAPIView.as_view(), name = 'add_materials'),
    path('material/edit/<str:item>/<int:pk>', MaterialsRetrieveUpdateDestroyAPIView.as_view(), name='edit_materials'),
    path('labour/add/<str:item>', LabourRelListCreateAPIView.as_view(), name = 'add_labour'),
    path('labour/edit/<str:item>/<int:pk>', LabourRelRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_labour'),
    path('tools/add/<str:item>', ToolsListCreateAPIView.as_view(), name = 'add_tools'),
    path('tools/edit/<str:item>/<int:pk>', ToolsRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_tools'),
    path('add/', GeneralAPUsListCreateAPIView.as_view(), name = 'apu_list'),
    path('edit/<int:pk>', APURetrieveUpdateDestroyAPIView.as_view(), name = 'apu_edit')
]