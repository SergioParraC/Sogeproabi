from django.urls import path
from apps.APUs.api.views.specific_views import MaterialRelListCreateAPIView, MaterialsRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('material/add/<str:item>', MaterialRelListCreateAPIView.as_view(), name = 'add_materials'),
    path('material/edit/<str:item>/<int:pk>', MaterialsRetrieveUpdateDestroyAPIView.as_view(), name='edit_materials')
]
