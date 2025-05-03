from django.core.management.base import BaseCommand
from equipment.models import EquipmentType

class Command(BaseCommand):
    help = 'Creates initial equipment types'

    def handle(self, *args, **options):
        EquipmentType.objects.get_or_create(
            id=1,
            defaults={
                'type_name': 'TP-Link TL-WR74',
                'mask_sn': 'XXAAAAAXAA'
            }
        )
        EquipmentType.objects.get_or_create(
            id=2,
            defaults={
                'type_name': 'D-Link DIR-300',
                'mask_sn': 'NXXAAXZXaa'
            }
        )
        self.stdout.write(self.style.SUCCESS('Successfully created equipment types'))

