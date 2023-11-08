from django.urls import path
from apps.APUs.api.views.specific_views import MaterialRelListCreateAPIView, MaterialsRelRetrieveUpdateDestroyAPIView, LabourRelListCreateAPIView, LabourRelRetriebeUpdateDestroyAPIView


urlpatterns = [
    path('material/add/<str:item>', MaterialRelListCreateAPIView.as_view(), name = 'add_materials'),
    path('material/edit/<str:item>/<int:pk>', MaterialsRelRetrieveUpdateDestroyAPIView.as_view(), name='edit_materials'),
    path('labour/add/<str:item>', LabourRelListCreateAPIView.as_view(), name = 'add_labour'),
    path('labour/edit/<str:item>/<int:pk>', LabourRelRetriebeUpdateDestroyAPIView.as_view(), name = 'edit_labour')
]
