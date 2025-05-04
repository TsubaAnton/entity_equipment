from .models import Equipment
from django.db.models import Q
from .serializers import EquipmentCreateSerializer, EquipmentUpdateSerializer
from rest_framework.exceptions import ValidationError, NotFound


def list_equipment(filters):
    """
    Возвращает Queryset оборудования,учитывая фильтрацию и поиск
    :param filters: request.query_params (QueryDict)
    :return: QuerySet[Equipment]
    """
    queryset = Equipment.objects.filter(is_deleted=False)
    if 'equipment_type' in filters:
        queryset = queryset.filter(equipment_type=filters['equipment_type'])
    search = filters.get('search')
    if search:
        queryset = queryset.filter(Q(serial_number__icontains=search) | Q(note__icontains=search))
    return queryset


def create_equipment(data):
    """
    Создает одну или несколько записей оборудования
    :param data: dict или list[dict] с полями equipment_type, serial_number и note
    :return: Объект Equipment или список объектов
    """
    items = data if isinstance(data, list) else [data]
    created = []
    errors = []
    for index, item in enumerate(items):
        serializer = EquipmentCreateSerializer(data=item)
        if serializer.is_valid():
            created.append(serializer.save())
        else:
            errors.append({index: serializer.errors})
    if errors:
        raise ValidationError(errors)
    return created if isinstance(data, list) else created[0]


def get_equipment(pk):
    """
    Возвращает запись Equipment по id
    """
    try:
        equipment = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExists:
        raise NotFound("Оборудование не найдено")
    return equipment


def update_equipment(pk, data):
    """
    Обновляет запись Equipment по id и возвращает ее
    """
    try:
        instance = get_equipment(pk)
        serializer = EquipmentUpdateSerializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
    except:
        raise NotFound("Оборудование отсутствует")


def delete_equipment(pk):
    """
    Мягкое удаление записи Equipment по id
    """
    instance = get_equipment(pk)
    instance.is_deleted = True
    instance.save()
    return instance




