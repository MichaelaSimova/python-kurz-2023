import json

with open("body.json", "r") as infile:
    body = json.load(infile)

prospech = {}

for student in body:
    if body[student] >= 60:
        prospech[student] = "Pass"
    else:
        prospech[student] = "Fail"

with open("prospech.json", "w") as outfile:
    json.dump(prospech, outfile, ensure_ascii=False, indent=4)