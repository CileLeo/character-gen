import random
import json

def generate():
    presetsFile = open("presets.json")
    presetsData = json.load(presetsFile)

    class Character():
        def __init__(self, countryInput, genderInput, nameInput, ageInput):
            self.country = countryInput
            self.gender = genderInput
            self.name = nameInput
            self.age = ageInput

    TEMPcountry = presetsData[random.randint(0, len(presetsData) - 1)]
    TEMPgenderList = TEMPcountry["genders"]
    TEMPgenderChance = []
    for gender in TEMPgenderList:
        TEMPgenderChance.append(gender["chance"])

    TEMPgender = random.choices(TEMPgenderList, weights = TEMPgenderChance, k=1)
    TEMPage = random.randint(TEMPgender[0]["min_age"], TEMPgender[0]["max_age"])
    TEMPname = random.choice(TEMPgender[0]["names"])

    return Character(
        TEMPcountry["country_name"],
        TEMPgender[0]["gender"],
        TEMPname,
        TEMPage
    )