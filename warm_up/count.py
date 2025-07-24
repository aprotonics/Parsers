from numpy import int32
from main.get import get_array
from main.clasterize import clasterize_array


count_limit = int32(1000000000)

for i in range(count_limit):
    numbers_array = get_array(i)
    numbers_array_stroke = str(numbers_array)
    numbers_array_stroke_length = len(numbers_array_stroke)

    array_length = int()

    file = "/home/time-traveller/macros/scripts/scripts_stage_six/"\
    "scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up.txt"


    with open(file=file, mode="rt", encoding="utf-8") as f:

        array = f.read()
        array_length = len(array)


    if numbers_array_stroke_length > array_length:

        numbers_array_clasterized = clasterize_array(numbers_array)

        file = "/home/time-traveller/macros/scripts/scripts_stage_six/"\
        "scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:

            for value in numbers_array_clasterized:
                value = str(value)
                value = value[1:-1]
                value += "\n"

                f.write(value)

            f.write("\n")
