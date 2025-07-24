from filter_unicode import filter_stroke


professions = []

professions_list = []
file = "/home/time-traveller/macros/scripts/cdh/formatted/filtered/hr_agency_apijob_jobs_2.txt"


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

    lexema_er = "er"
    lexema_or = "or"
    lexema_ine = "ine"

    lexemas = [lexema_er, lexema_or, lexema_ine]
    suffix_length = 6

    inappropriates = ["Partner", "Interactive", "Water", "Meyer", "Perimeter", "Power"]
    
    profession_formatted = profession.split(" ")

    for i in range(len(profession_formatted)):
        value = profession_formatted[i]
        value_lexema = value[-suffix_length:]

        if value in inappropriates:
            continue

        for j in range(len(lexemas)):
            lexema = lexemas[j]
            lexema_length = len(lexema)

            if value_lexema.rfind(lexema) != -1:
                lexema_index = value_lexema.rfind(lexema)

                if len(value_lexema) - lexema_index == lexema_length:
                    professions.append(value)
                else:
                    pass

print(len(professions))
print(professions[:5])
