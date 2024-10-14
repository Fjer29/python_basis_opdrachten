# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



#print(ord(' '))
#print(chr(122))

zin = input("Geef de tekst die je wilt encrypten: ")

character_codes = []
for teken in zin:
    if teken == ' ':
        character_codes.append(teken)
    elif 'a' <= teken <= 'z':
        new_code = ord(teken) + 5
        if new_code > ord('z'):
            new_code -= 26
        character_codes.append(chr(new_code))
    elif 'A' <= teken <= 'Z':
        new_code = ord(teken) + 5
        if new_code > ord('Z'):
            new_code -= 26
        character_codes.append(chr(new_code))
    else:
        character_codes.append(teken)

encrypted_zin = ''.join(character_codes)

print(encrypted_zin)
