
def is_simple(number: int) -> bool:
    number = number

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
