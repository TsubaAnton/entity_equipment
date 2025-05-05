import re
from rest_framework.serializers import ValidationError


def validate_number_matches_the_mask(serial_number: str, mask_sn: str) -> None:
    """
    Проверяет, что serial_number строго соответствует mask_sn.
    """
    mask = mask_sn.strip()
    if len(serial_number) != len(mask):
        raise ValidationError(
            f"Неправильная длина: ожидалось {len(mask)}, получено {len(serial_number)}"
        )
    regex_map = {
        'N': r'[0-9]',
        'A': r'[A-Z]',
        'a': r'[a-z]',
        'X': r'[A-Z0-9]',
        'Z': r'[-_@]'
    }

    pattern = '^'
    for idx, sym in enumerate(mask, start=1):
        if sym not in regex_map:
            raise ValidationError(
                f"Недопустимый символ в маске '{sym}' на позиции {idx}."
            )
        pattern += regex_map[sym]
    pattern += '$'

    if not re.fullmatch(pattern, serial_number):
        for i, (ch, sym) in enumerate(zip(serial_number, mask), start=1):
            if not re.fullmatch(regex_map[sym], ch):
                raise ValidationError(
                    f"Символ '{ch}' на позиции {i} не соответствует требованию '{sym}'"
                )
        raise ValidationError("Серийный номер не соответствует маске")

    return None
