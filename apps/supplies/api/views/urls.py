from django.urls import path
from apps.supplies.api.views.general_views import MaterialListCreateAPIView, MaterialRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('material/', MaterialListCreateAPIView.as_view(), name = 'material'),
    path('material/<int:pk>', MaterialRetrieveUpdateDestroyAPIView.as_view(), name = 'material_edit'),
]
