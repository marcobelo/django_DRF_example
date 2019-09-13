import json

with open("allys.json", "r") as file:
    alliances = json.load(file)

with open("alliances_effects.csv", "w") as file:
    for ally in alliances.keys():
        for quantity in alliances[ally]["effects"]:
            effect = alliances[ally]["effects"][quantity]
            line = f"{ally}|{quantity}|{effect}\n"
            file.write(line)
