# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

zijde1 = int(input("Geef de lengte van de eerste zijde: "))
zijde2 = int(input("Geef de lengte van de tweede zijde: "))

print ("De lengte van de schuine zijde is: ", math.sqrt(zijde1 ** 2 + zijde2 ** 2))