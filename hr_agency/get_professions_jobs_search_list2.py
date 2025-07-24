from filter_unicode import filter_stroke


professions = []

professions_list = []
file = "/home/time-traveller/macros/scripts/cdh/hr/formatted/filtered/hr_agency_jobs_search_jobs2.txt"


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

    profession = filter_stroke(profession)

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

    lexemas = [lexema_or, lexema_er, lexema_ist, lexema_ant, lexema_tect, lexema_ate, lexema_urse,
                lexema_tice, lexema_tive, lexema_ian, lexema_ic]
    suffix_length = 6

    inappropriates = ["Partner", "Interactive", "Super", "Greater", "Computer", "Disaster", "Summer"]
    
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
