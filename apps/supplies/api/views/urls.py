from django.urls import path
from apps.supplies.api.views.specific_views import *

urlpatterns = [
    path('material/add/', MaterialListCreateAPIView.as_view(), name = 'material_add'),
    path('material/edit/<int:pk>', MaterialRetrieveUpdateDestroyAPIView.as_view(), name = 'material_edit'),
    path('labour/add/', LabourListCreateAPIView.as_view(), name = 'labour_add'),
    path('labour/edit/<int:pk>', LabourRetrieveUpdateDestroyAPIView.as_view(), name = 'labour_edit'),
    path('tools/add/', ToolsListCreateAPIView.as_view(), name = 'labour_add'),
    path('tools/edit/<int:pk>', ToolsRetrieveUpdateDestroyAPIView.as_view(), name = 'labour_edit')
]
