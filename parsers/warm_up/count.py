from main.get import get_array


for i in range(10000000000):
    numbers_array = get_array(i)
    numbers_array = str(numbers_array)
    numbers_array_length = len(numbers_array)

    array_length = int()

    file = "txt.txt"

    with open(file=file, mode="rt", encoding="utf-8") as f:
        
        array = f.read()
        array_length = len(array)


    if numbers_array_length > array_length:


        file = "txt.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:

            f.write(numbers_array)

