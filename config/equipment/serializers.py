from .models import Equipment, EquipmentType
from rest_framework import serializers
from .validators import validate_equipment_data


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        read_only_fields = ('is_deleted',)

    def validate_serial_number(self, data):
        instance = self.instance
        serial_number = data.get('serial_number', instance.serial_number if instance else None)
        equipment_type = data.get('equipment_type', instance.equipment_type if instance else None)
        if serial_number and equipment_type:
            validate_equipment_data(serial_number=serial_number, equipment_type=equipment_type, instance=instance)
        return data


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ["equipment_type", "serial_number", "note"]

    def validate(self, data):
        validate_equipment_data(serial_number=data['serial_number'], equipment_type=data['equipment_type'])
        return data


class EquipmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        read_only_fields = ('serial_number', 'equipment_type',)
