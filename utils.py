import random
from enums import Format, Orientation, Color, Subject, TimeOfDay
from enum import Enum

def get_by_index(enum_cls: Enum, digit_char: str) -> str: 
    digit = int(digit_char)
    values = list(enum_cls)
    return values[digit % len(values)].value

def generate_challange(id: int) -> dict:
    id_str = str(id)

    return {
        "Format": get_by_index(Format, id_str[0]),
        "Orientation": get_by_index(Orientation, id_str[1]),
        "Color": get_by_index(Color, id_str[2]),
        "Subject": get_by_index(Subject, id_str[3]),
        "Time of Day": get_by_index(TimeOfDay, id_str[4]),
        "ID": id_str
    }

def generate_seed() -> int:
    new_id_str = ""

    format_idx = random.randrange(len(Format))
    new_id_str += str(format_idx + 1)

    enums = [Orientation, Color, Subject, TimeOfDay]

    for enum_cls in enums:
        new_id_str += str(random.randint(0, len(enum_cls) - 1))

    return int(new_id_str)