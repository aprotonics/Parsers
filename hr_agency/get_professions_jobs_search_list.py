from filter_unicode import filter_stroke_profession


professions = []

professions_list = []
file = "/home/time-traveller/macros/scripts/cdh/hr/formatted/filtered/hr_agency_jobs_search_jobs.txt"


with open(file=file, mode="rt", encoding="utf-8") as f:
    professions_list = f.readlines()


professions_list_length = len(professions_list)

for i in range(100):
    value = professions_list[i]

    value_formatted = value.split(", \"")
    profession = value_formatted[0]
    profession = profession[1:-1]
    company = value_formatted[1]
    company = company[:-1]
    town = value_formatted[2]
    town = town.rstrip()
    town = town[:-1]

    profession = filter_stroke_profession(profession)

    lexema_r = "r"
    lexema_ist = "ist"
    lexema_ant = "ant"
    lexema_tect = "tect"
    lexema_ate = "ate"
    lexema_tive = "tive"

    lexema_or = "or"
    lexema_er = "er"
    lexema_ist = "ist"
    lexema_ant = "ant"
    lexema_tect = "tect"
    lexema_ate = "ate"
    lexema_urse = "urse"
    lexema_tice = "tice"
    lexema_tive = "tive"
    lexema_ian = "ian"
    lexema_ic = "ic"

    lexema_or = "or"
    lexema_er = "er"
    lexema_ist = "ist"
    lexema_yst = "yst"
    lexema_ant = "ant"
    lexema_ident = "ident"
    lexema_tect = "tect"
    lexema_ate = "ate"
    lexema_tive = "tive"
    lexema_etary = "etary"

    lexema_or = "or"
    lexema_er = "er"
    lexema_ist = "ist"
    lexema_yst = "yst"
    lexema_ant = "ant"
    lexema_ident = "ident"
    lexema_tect = "tect"
    lexema_ate = "ate"
    lexema_tive = "tive"
    lexema_ief = "ief"

    lexemas = [lexema_r, lexema_ist, lexema_ant, lexema_tect, lexema_ate, lexema_tive]
    suffix_length = 6

    inappropriates = ["Partner", "Interactive"]
    inappropriates2 = ["Partner", "Interactive", "Super", "Greater", "Computer", "Disaster", "Summer"]
    inappropriates3 = ["Partner", "Interactive", "Customer", "Corporate", "Center", "Year", "Temporary"]
    inappropriates4 = ["Partner", "Interactive", "Summer", "Late", "Cashier", "Corporate", "Water"]

    profession_formatted = profession.split(" ")

    for j in range(len(profession_formatted)):
        value = profession_formatted[j]
        value_lexema = value[-suffix_length:]

        if value in inappropriates:
            continue

        for k in range(len(lexemas)):
            lexema = lexemas[k]
            lexema_length = len(lexema)

            if lexema != value:
                if value_lexema.rfind(lexema) != -1:
                    lexema_index = value_lexema.rfind(lexema)

                    if len(value_lexema) - lexema_index == lexema_length:
                        professions.append(value)
                    else:
                        pass

print(len(professions))
print(professions[:5])
