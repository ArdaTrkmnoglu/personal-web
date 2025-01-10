#A. Arda Türkmenoğlu - 150230056

import auction_operations as ao
import math

name = input("The organizer, please enter your full name (First_Name <Other Names if any> Last_Name): ")
organizer_name = ao.name_formatter(name)

organizer_information = {"Name": organizer_name}

print(f"{organizer_name} is organising this event.")

participants = [organizer_information]

participant_names = []
participant_ages = []
participant_budgets = []
participant_famescores = []

while True:
    fullname_input = input("Enter your full name (First_Name <Other Names if any> Last_Name): ")
    if fullname_input.upper() == "DONE":
        break

    formatted_name = ao.name_formatter(fullname_input)

    is_agent, agent_name = ao.check_secret_agent(formatted_name)
    if is_agent:
        print(f"{agent_name} is caught and not allowed to participate.")
        print(f"Reason: {"Risk of espionage" if agent_name == "James Bond" else  "Risk of assasination"}")
        continue
    else:
        participant_names.append(formatted_name)

    age = int(input("Enter your age: "))
    participant_ages.append(age)

    budget = float(input("Enter your budget: "))
    participant_budgets.append(budget)

    fame = int(input("How famous are you? "))
    participant_famescores.append(fame)

participant_information = ao.participant_information_merger(participant_names, participant_ages, participant_budgets, participant_famescores)

intruders = ao.check_intruders(participant_information)

allowed_participants = []

for participant in participant_information:
    if participant["Name"] in intruders:
        print(f"{participant["Name"]} is not allowed to participate.")
        print("Reason: {}".format("Underage" if participant["Age"] < 18 else "Insufficient budget" if participant["Budget"] < 5000 else "Not famous enough"))

    else:
        allowed_participants.append(participant)

participants.extend(allowed_participants)

sorted_participants = sorted(participants, key=lambda x: x.get("Budget", math.inf), reverse=True)

print("Participants:")
for participant in sorted_participants:
    if len(participant) == 1:
        print(f"{participant['Name']}: The Organizer")
    else:
        print("{name}: {age} years old, Budget: ${budget:.2f} and has a fame of {fame} points.".format(name = participant["Name"], age = participant["Age"], budget = participant["Budget"], fame = participant["Fame"]))
