from filter_unicode import filter_stroke_company


companies = []

companies_list = []
file = "/home/time-traveller/macros/scripts/cdh/hr/formatted/filtered/hr_agency_jobs_search_jobs.txt"


with open(file=file, mode="rt", encoding="utf-8") as f:
    companies_list = f.readlines()


companies_list_length = len(companies_list)
print(companies_list_length)
print()

for i in range(companies_list_length):
    value = companies_list[i]

    value_formatted = value.split(", \"")
    profession = value_formatted[0]
    profession = profession[1:-1]
    company = value_formatted[1]
    company = company[:-1]
    town = value_formatted[2]
    town = town.rstrip()
    town = town[:-1]

    if len(company):
        pass
    
    company = filter_stroke_company(company)

    lexema_inc = "Inc"
    lexema_inc3 = "INC"
    lexema_llc = "LLC"
    lexema_llp = "LLP"
    lexema_gmbh = "GmbH"
    lexema_co = "Co"

    lexema_company = "Company"
    lexema_company2 = "COMPANY"
    lexema_company3 = "company"
    lexema_company4 = "Companies"
    lexema_mutual = "Mutual"
    lexema_agency = "Agency"
    lexema_alliance = "Alliance"
    lexema_community = "Communities"
    lexema_group = "Group"
    lexema_corp = "Corp"
    lexema_corp2 = "Corporation"
    lexema_corp3 = "Incorporated"
    lexema_intern = "International"
    lexema_associate = "Associates"
    lexema_associate2 = "And"
    lexema_associate3 = "Head"
    lexema_trust = "TRUST"
    lexema_coalition = "Coalition"

    lexema_communicate = "Communications"
    lexema_communicate2 = "COMMUNICATIONS"
    lexema_consult = "Consulting"
    lexema_manage = "Management"
    lexema_manage2 = "management"
    lexema_advice = "Advisors"
    lexema_assure = "Assurance"
    lexema_health = "Health"
    lexema_health2 = "Healthcare"
    lexema_health3 = "Care"
    lexema_med = "Medicinals"
    lexema_therapy = "Therapeutics"
    lexema_live = "Living"
    lexema_pharma = "Pharmaceuticals"
    lexema_biopharma = "Biopharmaceuticals"

    lexema_system = "Systems"
    lexema_solution = "Solutions"
    lexema_shipment = "Shipments"
    lexema_industry = "Industries"
    lexema_tech = "Technologies"

    lexema_credit = "Credit"
    lexema_credit2 = "Union"

    lexema_hold = "Holdings"
    lexema_venture = "Ventures"

    lexemas = [lexema_inc, lexema_inc3, lexema_llc, lexema_llp, lexema_gmbh, lexema_co, lexema_company, lexema_company2, lexema_company3,
                lexema_company4, lexema_mutual, lexema_agency, lexema_alliance, lexema_community, lexema_group, lexema_corp, lexema_corp2,
                lexema_corp3, lexema_intern, lexema_associate, lexema_associate2, lexema_associate3, lexema_trust,
                lexema_coalition, lexema_system, lexema_solution, lexema_shipment, lexema_industry, lexema_tech,
                lexema_communicate, lexema_communicate2, lexema_consult, lexema_manage, lexema_manage2, lexema_advice, lexema_assure,
                lexema_health, lexema_health2, lexema_health3, lexema_med, lexema_therapy, lexema_live, lexema_pharma,
                lexema_biopharma, lexema_credit, lexema_credit2, lexema_hold, lexema_venture]
    suffix_length = 3
    black_list_companies = ["Parents", "Partner", "Partners", "Interactive", "Recruitment", "Recruiters", "Second", "Later", "Year",
                            "Personnel", "Staffing", "Remotely", "Site", "Bread"]

    company_formatted = company.split(" ")
    lexema_index_value = 0
    lexemas_indices = []

    for j in range(len(company_formatted)):
        value = company_formatted[j]
        
        for lexema in lexemas:
            if value == lexema:
                lexema_index_value = j
                lexemas_indices.append(lexema_index_value)
    
    if len(lexemas_indices) > 0:
        company_formatted_copy = ""

        for j in range(len(company_formatted)):
            if j not in lexemas_indices:
                company_formatted_copy += company_formatted[j] + " "

        company_formatted_copy = company_formatted_copy.rstrip()
        company_formatted = ""
        company_formatted = company_formatted_copy

    company_in_black_list = False

    if type(company_formatted) == type([]):
        for value in company_formatted:
            if value in black_list_companies:
                company_in_black_list = True

        if company_in_black_list:
            continue
        
        company_formatted_str = ""

        for value in company_formatted:
            company_formatted_str += value + " "
        
        company_formatted_str = company_formatted_str.rstrip()
        company_formatted = company_formatted_str

    if len(company_formatted):
        companies.append(company_formatted)

print(len(companies))
print()
print(companies[:5])
print()

for value in companies:
    if value == "Google":
        print(value)

print()
