import re
from rest_framework.serializers import ValidationError


def validate_number_matches_the_mask(serial_number, mask_sn):
    regex_pattern = {
        'N': r'[0-9]',
        'A': r'[A-Z]',
        'a': r'[a-z]',
        'X': r'[A-Z0-9]',
        'Z': r'[-_@]'
    }
    if len(serial_number) != len(mask_sn):
        raise ValidationError("Номер невалиден, разная длина")

    number = '^'
    for symbol in mask_sn:
        if symbol in regex_pattern:
            number += regex_pattern[symbol]
        else:
            raise ValidationError(f'Недопустимый символ: {symbol}')
    number += '$'
    if not re.fullmatch(number, serial_number):
        raise ValidationError('Серийный номер не соответствует маске')
