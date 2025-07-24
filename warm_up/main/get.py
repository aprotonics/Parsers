from main.check_value import is_simple


def get_array(upper_number: int) -> list:
    upper_number = upper_number

    numbers_array = []

    for i in range(upper_number + 1):

        is_simple_number = is_simple(i)

        if is_simple_number:
            numbers_array.append(i)

    return numbers_array
