from django.db import models
from django.core.validators import RegexValidator
from .validators import validate_number_matches_the_mask

NULLABLE = {'blank': True, 'null': True}


class EquipmentType(models.Model):
    type_name = models.CharField(max_length=255, verbose_name='Наименование типа')
    mask_sn = models.CharField(max_length=255, verbose_name='Маска серийного номера',
                               validators=[RegexValidator(regex='^[NAaXZ]+$')])

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Тип оборубования'
        verbose_name_plural = 'Типы оборудования'


class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, verbose_name='Код типа оборудования')
    serial_number = models.CharField(max_length=255, verbose_name='Серийный номер')
    note = models.TextField(verbose_name='Примечание', **NULLABLE)
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f"{self.equipment_type} - {self.serial_number}"

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'
        unique_together = ('equipment_type', 'serial_number')
