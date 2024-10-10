# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

file1 = open("vragenlijst.txt", "at")
file1.write(f"{vraag1} \n")
file1.write(f"{vraag2} \n")
file1.write(f"{vraag3} \n")