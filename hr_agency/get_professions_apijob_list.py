from filter_unicode import filter_stroke


professions = []

professions_list = []
file = "/home/time-traveller/macros/scripts/cdh/formatted/filtered/hr_agency_apijob_jobs.txt"


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

    lexema_ista = "ista"
    lexema_er = "er"
    lexema_ist = "ist"
    lexema_ert = "ert"
    lexema_tect = "tect"
    lexema_ate = "ate"
    lexema_ian = "ian"
    lexema_ol = "ol"
    lexema_ic = "ic"

    lexema_er = "er"
    lexema_or = "or"
    lexema_ine = "ine"
    
    lexema_ent = "ent"

    lexema_ant = "ant"

    lexemas = [lexema_ista, lexema_er, lexema_ist, lexema_ert, lexema_tect, lexema_ate, lexema_ian, lexema_ol, lexema_ic]
    suffix_length = 6

    inappropriates = ["Partner", "Interactive"]
    inappropriates2 = ["Partner", "Interactive", "Water", "Meyer", "Perimeter", "Power"]
    inappropriates3 = ["Partner", "Interactive"]
    inappropriates4 = ["Partner", "Interactive"]
    
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
