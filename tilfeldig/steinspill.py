n = int(input("Skriv et heltall som passer bra."))

steiner = n

# Simulasjon er egentlig ikke nødvendig. Kan bare sjekke om det er oddetall eller partall.

# if steiner % 2 == 0:
#     print("Ola")
# else:
#     print("Kari")

# Her er simulasjon allikevel:

while steiner > 1:
    steiner -= 2

else:
    if steiner == 1:
        print("Kari")
    elif steiner == 0:
        print("Ola")
    else:
        print("Noe er galt.")
