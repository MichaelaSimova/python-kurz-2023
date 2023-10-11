import json

with open("body.json", "r", encoding="utf-8") as infile:
    pocet_bodu = json.load(infile)

prospech = []

for student in pocet_bodu:
    if pocet_bodu[student] >= 60:
        prospech[student] = "Pass"
    else:
        prospech[student] = "Fail"

with open("prospech.json", "w",encoding="utf-8") as outfile:
    json.dump(prospech, outfile, ensure_ascii=False,)