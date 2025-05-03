from .models import Equipment, EquipmentType
from rest_framework import serializers
from .validators import validate_number_matches_the_mask


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        read_only_fields = ('is_deleted',)

    def validate_serial_number(self, value):
        instance = self.instance
        equipment_type = instance.equipment_type
        validate_number_matches_the_mask(value, equipment_type.mask_sn)
        if Equipment.objects.filter(equipment_type=equipment_type, serial_number=value).exclude(id=instance.id).exists():
            raise serializers.ValidationError("Серийный номер занят")
        return value


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ["equipment_type", "serial_number", "note"]

    def validate(self, data):
        equipment_type = data["equipment_type"]
        serial_number = data["serial_number"]
        validate_number_matches_the_mask(serial_number, equipment_type.mask_sn)
        if Equipment.objects.filter(equipment_type=equipment_type, serial_number=serial_number).exists():
            raise serializers.ValidationError({'serial_number': 'Серийный номер уже существует'})
        return data
    