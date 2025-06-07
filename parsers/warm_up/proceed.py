import os
from main.get import get_array


inner_text = ""
file = "/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/txt.txt"


with open(file=file, mode="rt", encoding="utf-8") as f:
    
    inner_text = f.read()


inner_text = inner_text[1:len(inner_text)-1]
inner_text = inner_text.split(", ")
last_value = inner_text[len(inner_text)-1]
last_value = int(last_value)

for i in range(last_value + 1, 10000000000):
    numbers_array = get_array(i)
    numbers_array = str(numbers_array)
    numbers_array_length = len(numbers_array)


    with open(file=file, mode="rt", encoding="utf-8") as f:
        
        array = f.read()
        array_length = len(array)



    if numbers_array_length > array_length:
        

        with open(file=file, mode="wt", encoding="utf-8") as f:

            f.write(numbers_array)
