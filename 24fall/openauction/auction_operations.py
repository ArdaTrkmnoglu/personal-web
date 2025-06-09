#A. Arda Türkmenoğlu - 150230056

def name_formatter(fullnameinput):
    splitted_fullname = fullnameinput.split(" ")

    formatted_fullname_list = []

    for name in splitted_fullname[:-1]:
        formatted_fullname_list.append(name.capitalize())

    formatted_fullname_list.append(splitted_fullname[-1].upper())

    formatted_fullname = " ".join(formatted_fullname_list)
    return formatted_fullname


def check_secret_agent(name):
    encoded_name = name.lower().replace(" ", "")[::-1]

    if encoded_name == "dnobsemaj" or "bond" in encoded_name:
        return True, "James Bond"
    
    elif "47" in encoded_name or "74" in encoded_name:
        return True, "Agent 47"
    
    else:
        return False, None
    

def participant_information_merger(namelist, agelist, budgetlist, famescorelist):

    participant_information = []

    for name, age, budget, fame in zip(namelist, agelist, budgetlist, famescorelist):
        participant_data = {"Name": name, "Age": age, "Budget": budget, "Fame": fame}
        participant_information.append(participant_data)

    return participant_information

def check_intruders(participant_information):
    intruders = []

    for participant in participant_information:
        if participant["Age"] < 18 or participant["Budget"] < 5000 or participant["Fame"] < 50:
            intruders.append(participant["Name"])

    return intruders
