from django.urls import path
from apps.APUs.api.views.general_views import MaterialRelListCreateAPIView

urlpatterns = [
    path('material/add/', MaterialRelListCreateAPIView.as_view(), name = 'add_materials')
]
