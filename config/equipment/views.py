from .models import EquipmentType
from rest_framework import generics, filters, status
from .serializers import EquipmentSerializer, EquipmentTypeSerializer
from .paginators import EquipmentPaginator
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .services import list_equipment, create_equipment, get_equipment, update_equipment, delete_equipment
from rest_framework_simplejwt.views import TokenObtainPairView


class EquipmentListCreateAPIView(generics.GenericAPIView):
    """
    get: Вывод пагинированного списка оборудования с возможностью фильтрации по типу и поиска
    post: Создание новой(ых) записи(ей)
    """
    permission_classes = [IsAuthenticated]
    pagination_class = EquipmentPaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
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
    put: Редактирование записи
    delete: Удаление записи (мягкое удаление)
    """
    permission_classes = [IsAuthenticated]

    def get(request, id):
        obj = get_equipment(id)
        serializer = EquipmentSerializer(obj)
        return Response(serializer.data)

    def put(self, request, id):
        obj = update_equipment(id, request.data)
        serializer = EquipmentSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, id):
        delete_equipment(id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentTypeListAPIView(generics.ListAPIView):
    """
    get: - Вывод пагинированного списка типов оборудования
         - Возможность фильтрации по наименованию и поиска по mask_sn
    """
    permission_classes = [IsAuthenticated]
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    pagination_class = EquipmentPaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type_name']
    search_fields = ['type_name', 'mask_sn']


class UserLoginAPIView(TokenObtainPairView):
    """
    post: Авторизация пользователя (выпуск токена)
    """
    permission_classes = []
    authentication_classes = []

# class EquipmentListAPIView(generics.ListAPIView):
#     serializer_class = EquipmentSerializer
#     queryset = Equipment.objects.filter(is_deleted=False)
#     pagination_class = EquipmentPaginator
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['equipment_type']
#     search_fields = ['serial_number', 'note']
#     permission_classes = [IsAuthenticated]
#
#
# class EquipmentCreateAPIView(generics.CreateAPIView):
#     serializer_class = EquipmentCreateSerializer
#     queryset = Equipment.objects.all()
#     permission_classes = [IsAuthenticated]
#
#     def create(self, request, *args, **kwargs):
#         many = isinstance(request.data, list)
#         serializer = self.get_serializer(data=request.data, many=many)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
# class EquipmentDetailAPIView(generics.RetrieveAPIView):
#     serializer_class = EquipmentSerializer
#     queryset = Equipment.objects.filter(is_deleted=False)
#     permission_classes = [IsAuthenticated]
#
#
# class EquipmentUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = EquipmentSerializer
#     queryset = Equipment.objects.filter(is_deleted=False)
#     permission_classes = [IsAuthenticated]
#
#
# class EquipmentDeleteAPIView(generics.DestroyAPIView):
#     serializer_class = EquipmentSerializer
#     queryset = Equipment.objects.filter(is_deleted=False)
#     permission_classes = [IsAuthenticated]
#
#     def perform_destroy(self, instance):
#         instance.is_deleted = True
#         instance.save()
#
#
# class EquipmentTypeListAPIView(generics.ListAPIView):
#     serializer_class = EquipmentTypeSerializer
#     queryset = EquipmentType.objects.all()
#     pagination_class = EquipmentPaginator
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['type_name']
#     search_fields = ['type_name', 'mask_sn']
#     permission_classes = [IsAuthenticated]
