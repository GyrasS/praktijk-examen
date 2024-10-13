print("Wat is je leeftijd?")
leeftijd = int(input("Voer het aantal jaren in: ")) # invoer van leeftijd
print("Wat is je werkstatuut?")
werk = input(f"Voer in: medewerker, zelfstandige of ambtenaar: ") # invoer van werkstatuut

werkstatuut = {"medewerker" : [350, 20], "zelfstandige" : [300, 15], "ambtenaar" : [370, 25]} # dictionary, keys is de werkstatuut en values zijn lists met daar in de hoeveelheid euro

def pensioen(leeftijd, werk, werkstatuut):
    if leeftijd < 65:
        verschil = 65 - leeftijd # berekend het verschil tussen het pensioen leeftijd, en de ingevoerde leeftijd
        return f"Van werken word je gelukkig, je mag nog {verschil} jaar genieten van je baan" # uitvoer als leeftijd te laag is
    else:
        if leeftijd < 70:
            return f"Je krijgt € {werkstatuut[werk][0]} per week." # uitvoer als leeftijd 65 tot 70 is
        else:
            return f"Je krijgt € {werkstatuut[werk][0] + werkstatuut[werk][1]} per week." # uitvoer als leeftijd boven 70 is
print(pensioen(leeftijd, werk, werkstatuut))