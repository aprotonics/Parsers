import json


def clasterize_array(numbers_array: list) -> list:
    numbers_array = numbers_array

    numbers_strokes = []
    numbers_stroke = []

    for i in range(len(numbers_array)):
        number_length = len(str(numbers_array[i]).split(", ")[0])

        match number_length:
            case 4:
                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 28:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case 5:
                if len(numbers_stroke) == 25:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 24:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case 6:
                if len(numbers_stroke) == 21:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 20:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case 7:
                if len(numbers_stroke) == 19:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 18:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case 8:
                if len(numbers_stroke) == 17:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 16:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case 9:
                if len(numbers_stroke) == 16:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 15:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case 10:
                if len(numbers_stroke) == 14:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

                numbers_stroke.append(numbers_array[i])

                if len(numbers_stroke) == 13:
                    numbers_strokes.append(numbers_stroke)
                    numbers_stroke = []

            case _:
                pass

        if i == len(numbers_array)-1:
            last_numbers_stroke = numbers_stroke

    numbers_strokes.append(last_numbers_stroke)

    return numbers_strokes
