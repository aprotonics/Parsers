def filter_stroke_profession(str_to_format):
    str_to_format = str_to_format
    
    symbols_to_filter = [",", "(", ")", ":", "-", "&", "#", "|", "/"]
    symbols_to_filter_with_empty = [",", "(", ")", ":", "-"]
    symbols_to_filter_with_additional_empty = ["&", "#", "|"]
    symbols_to_filter_without_empty = ["/"]

    for i in range(len(symbols_to_filter)):
        symbol_to_filter = symbols_to_filter[i]
        
        while symbol_to_filter in str_to_format:
            symbol_index = str_to_format.find(symbol_to_filter)

            match str_to_format[symbol_index]:
                case ",":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case "(":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case ")":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case ":":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case "-":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case "&":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+2:]
                case "#":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+2:]
                case "|":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+2:]
                case "/":
                    str_to_format = str_to_format[:symbol_index] + " " + str_to_format[symbol_index+1:]
                case _:
                    pass

    str_formatted = str_to_format

    return str_formatted


def filter_stroke_company(str_to_format):
    str_to_format = str_to_format

    symbols_to_filter = [",", ";", "-", "|", ".", "/", "&", ":", "(", ")", "+"]

    for i in range(len(symbols_to_filter)):
        symbol_to_filter = symbols_to_filter[i]

        while symbol_to_filter in str_to_format:
            symbol_index = str_to_format.find(symbol_to_filter)

            match str_to_format[symbol_index]:
                case ",":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case ";":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case ".":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case "/":
                    str_to_format = str_to_format[:symbol_index] + " " + str_to_format[symbol_index+1:]
                case "-":
                    str_to_format = str_to_format[:symbol_index-1] + str_to_format[symbol_index+1:]
                case "|":
                    str_to_format = str_to_format[:symbol_index-1] + str_to_format[symbol_index+1:]
                case "&":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case ":":
                    str_to_format = str_to_format[:symbol_index-1] + str_to_format[symbol_index+1:]
                case "+":
                    str_to_format = str_to_format[:symbol_index-1] + str_to_format[symbol_index+1:]
                case "(":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case ")":
                    str_to_format = str_to_format[:symbol_index] + str_to_format[symbol_index+1:]
                case _:
                    pass

    str_formatted = str_to_format.rstrip()

    return str_formatted
