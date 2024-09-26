# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

steden = []
for _ in range(5):
    stad = input("Voer een stad in: ")
    steden.append(stad)

#list.append(input("Stad 1: "))
#list.append(input("Stad 2: "))
#list.append(input("Stad 3: "))
#list.append(input("Stad 4: "))
#list.append(input("Stad 5: "))

steden.sort(reverse=True)
print(steden)