# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

poging = 0
raad = 0
while geheim_getal != raad:
    raad = int(input("raad het getal: "))
    if raad < 1 or raad > 100:
        print("Fout, het getal ligt tussen 1 en 100, probeer het opnieuw")
        quit()
    elif geheim_getal > raad:
        print("Het getal is hoger.")
    elif raad > geheim_getal:
        print("Het getal is lager")
    poging+=1


if poging == 1:
    print("Gefeliciteerd, je hebt het getal in", poging, "poging geraden!")
else:
    print("Gefeliciteerd, je hebt het getal in", poging, "pogingen geraden!")