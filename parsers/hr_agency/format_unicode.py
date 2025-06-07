def format_stroke(str_to_format):
    str_to_format = str_to_format
   
    str_formatted = ""
    words_with_unicode_number = len(str_to_format.split("\\")) - 1
    formatted_str = ""

    DICT = {
                "u00c9": "201",
                "u00e8": "232",
                "u00e9": "233",
                "u00eb": "235",
                "u00fc": "252",
            }

    match words_with_unicode_number:
        case 0:
            formatted_str = str_to_format
            return formatted_str

        case 1:
            for value in str_to_format:
                counter = 0
    
                if value == "\\" and counter < 1:
                    value = ""
                    counter += 1

                str_formatted += value

            if len(str_to_format.split("\\")) == 2:
                stroke = f"{str_to_format.split("\\")[1][:5]}"

            formatted_str = str_to_format.split("\\")[0] + chr(int(DICT[stroke])) + str_to_format.split("\\")[1][5:]

        case 2:
            if len(str_to_format.split("\\")) == 3:
                stroke = f"{str_to_format.split("\\")[1][:5]}"
                stroke2 = f"{str_to_format.split("\\")[2][:5]}"

            formatted_str = str_to_format.split("\\")[0] + chr(int(DICT[stroke])) + str_to_format.split("\\")[1][5:] \
                + chr(int(DICT[stroke2])) + str_to_format.split("\\")[2][5:]

    return formatted_str
