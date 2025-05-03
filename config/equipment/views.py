from .models import Equipment, EquipmentType
from rest_framework import generics, filters, status
from .serializers import EquipmentSerializer, EquipmentTypeSerializer, EquipmentCreateSerializer
from .paginators import EquipmentPaginator
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class EquipmentListAPIView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.filter(is_deleted=False)
    pagination_class = EquipmentPaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['equipment_type']
    search_fields = ['serial_number', 'note']
    permission_classes = [IsAuthenticated]


class EquipmentCreateAPIView(generics.CreateAPIView):
    serializer_class = EquipmentCreateSerializer
    queryset = Equipment.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EquipmentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]


class EquipmentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]


class EquipmentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class EquipmentTypeListAPIView(generics.ListAPIView):
    serializer_class = EquipmentTypeSerializer
    queryset = EquipmentType.objects.all()
    pagination_class = EquipmentPaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type_name']
    search_fields = ['type_name', 'mask_sn']
    permission_classes = [IsAuthenticated]
