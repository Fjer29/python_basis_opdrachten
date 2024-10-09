# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijden = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
leeftijd = int(input("Wat is uw leeftijd? "))

if leeftijden["baby"][0] <= leeftijd <= leeftijden["baby"][1]:
    print("U behoort tot de groep baby's")
    print("Daarom krijgt u", kortings_percentages["baby"], "% korting")
    print("U betaald daarom", (100 - kortings_percentages["baby"] / 100) * normale_toegangsprijs)

elif leeftijden["kinderen"][0] <= leeftijd <= leeftijden["kinderen"][1]:
    print("U behoort tot de groep kinderen")
    print("Daarom krijgt u", kortings_percentages["kinderen"], "% korting")
    print("U betaald daarom", (1 - kortings_percentages["kinderen"] / 100) * normale_toegangsprijs)

elif leeftijden["volwassenen"][0] <= leeftijd <= leeftijden["volwassenen"][1]:
    print("U behoort tot de groep volwassenen")
    print("Daarom krijgt u", kortings_percentages["volwassenen"], "% korting")
    print("U betaald daarom", (1 - kortings_percentages["volwassenen"] / 100) * normale_toegangsprijs)

elif leeftijden["ouderen"][0] <= leeftijd <= leeftijden["ouderen"][1]:
    print("U behoort tot de groep ouderen")
    print("Daarom krijgt u", kortings_percentages["ouderen"], "% korting")
    print("U betaald daarom", (1 - kortings_percentages["ouderen"] / 100) * normale_toegangsprijs)