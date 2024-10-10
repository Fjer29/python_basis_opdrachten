# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...
kosten = None
for topping in toppings:
    if topping[0] == keuze:
        kosten = topping[1]
        break


if kosten is not None:
    print("u heeft", keuze, "besteld, dat kost", kosten)
else:
    print("Uw keuze zit niet in ons assortiment")