from .apps import EquipmentConfig
from django.urls import path
from .views import EquipmentListCreateAPIView, EquipmentRetrieveUpdateDestroyAPIView, EquipmentTypeListAPIView, UserLoginAPIView

app_name = EquipmentConfig.name

urlpatterns = [
    path("api/equipment", EquipmentListCreateAPIView.as_view(), name="equipment_list_create"),
    path("api/equipment/<int:pk>", EquipmentRetrieveUpdateDestroyAPIView.as_view(), name="equipment_detail"),
    path("api/equipment-type", EquipmentTypeListAPIView.as_view(), name="equipment_type_list"),
    path("api/user/login", UserLoginAPIView.as_view(), name="user-login"),
]
