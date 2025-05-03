from .apps import EquipmentConfig
from django.urls import path
from .views import EquipmentListAPIView, EquipmentCreateAPIView, EquipmentDetailAPIView, EquipmentUpdateAPIView, EquipmentDeleteAPIView, EquipmentTypeListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = EquipmentConfig.name

urlpatterns = [
    path("api/equipment", EquipmentListAPIView.as_view(), name="equipment_list"),
    path("api/equipment/{id}", EquipmentDetailAPIView.as_view(), name="equipment_detail"),
    path("api/equipment", EquipmentCreateAPIView.as_view(), name="equipment_create"),
    path("api/equipment/{id}", EquipmentUpdateAPIView.as_view(), name="equipment_update"),
    path("api/equipment/{id}", EquipmentDeleteAPIView.as_view(), name="equipment_delete"),
    path("api/equipment-type", EquipmentTypeListAPIView.as_view(), name="equipment_type_list"),
    path("api/user/login", TokenObtainPairView.as_view(), name="user-login"),
]
