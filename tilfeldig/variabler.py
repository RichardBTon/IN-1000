print("Hei student!")

# NAVNEOPPGAVE

print("Navneoppgave")

# Ber om navn
navn = input("""
Skriv et navn
>>> """)

print(f"Hei {navn}!")

# Ber om nytt navn
sekundærnavn = input("""
Skriv et nytt navn
>>> """)

# Legger sammen navnene
sammen = navn + sekundærnavn
print(sammen)

#Gjør det samme, men med et " og " i midten
sammen = navn + " og " + sekundærnavn
print(sammen)


# TALLOPPGAVE

print()
print("Talloppgave:")

# Definerer tall
tall_1 = 10
tall_2 = 7

print(tall_1)
print(tall_2)

# Finner differansen
differanse = tall_1 - tall_2

print(differanse)
