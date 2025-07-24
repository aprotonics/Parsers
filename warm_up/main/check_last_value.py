from typing import Tuple
from main.check_value import is_simple


def is_last_simple(numbers_array: list) -> Tuple[bool, int]:
    numbers_array = numbers_array
    last_value = int()

    last_value = int(numbers_array[len(numbers_array)-1])
    is_last_simple = is_simple(last_value)

    return is_last_simple, last_value
