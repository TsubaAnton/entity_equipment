from .models import EquipmentType, Equipment
from rest_framework import generics, filters, status
from .serializers import EquipmentSerializer, EquipmentTypeSerializer
from .paginators import EquipmentPaginator
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .services import list_equipment, create_equipment, get_equipment, update_equipment, delete_equipment
from rest_framework_simplejwt.views import TokenObtainPairView


class BaseEquipmentView:
    pagination_class = EquipmentPaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class EquipmentListCreateAPIView(BaseEquipmentView, generics.ListCreateAPIView):
    """
    get: Вывод пагинированного списка оборудования с возможностью фильтрации по типу и поиска
    post: Создание новой(ых) записи(ей)
    """
    permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.filter(is_deleted=False).order_by('id')
    filterset_fields = ['equipment_type']
    search_fields = ['serial_number', 'note']

    def get(self, request):
        queryset = list_equipment(request.query_params)
        page = self.paginate_queryset(queryset)
        serializer = EquipmentSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        obj = create_equipment(request.data)
        many = isinstance(request.data, list)
        serializer = EquipmentSerializer(obj, many=many)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EquipmentRetrieveUpdateDestroyAPIView(generics.GenericAPIView):
    """
    get: Запрос данных по id
    put / patch: Редактирование записи
    delete: Удаление записи (мягкое удаление)
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        obj = get_equipment(pk)
        serializer = EquipmentSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = update_equipment(pk, request.data, partial=False)
        serializer = EquipmentSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        obj = update_equipment(pk, request.data, partial=True)
        serializer = EquipmentSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        delete_equipment(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentTypeListAPIView(BaseEquipmentView, generics.ListAPIView):
    """
    get: - Вывод пагинированного списка типов оборудования
         - Возможность фильтрации по наименованию и поиска по mask_sn
    """
    permission_classes = [IsAuthenticated]
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    filterset_fields = ['type_name']
    search_fields = ['type_name', 'mask_sn']


class UserLoginAPIView(TokenObtainPairView):
    """
    post: Авторизация пользователя (выпуск токена)
    """
    permission_classes = []
    authentication_classes = []

