# Oppgave:
# Skriv et program med en variabel som er et tall mellom 1 og 100.
# Brukeren skal gjette hvilket tall programmet "tenker på".
# Tilbakemeldinger gis ved at programmet printer ut "høyere" hvis tallet er for lavt, og "lavere" hvis det er for høyt.
# Når tallet er gjettet skal brukeren bli gratulert, og det skal stå hvor mange gjett som ble brukt.

# Program:
from random import randint


def intro():
    print("Velkommen til dette spillet!")
    print("Du skal prøve å gjette et tall mellom 1 og 100 ved å få tilbakemeldinger på om gjettet ditt var for lavt eller for høyt.")


def spør_gjetning():
    return int(input("Gjett et tall: "))


def tilbakemelding(gjetning):
    if gjetning < hemmelig_tall:
        print("For lavt!")

    elif gjetning > hemmelig_tall:
        print("For høyt!")

    else:
        print(
            f"Gratulerer! Du klarte å gjette tallet! Du brukte {gjett} gjett.")


intro()

hemmelig_tall = randint(1, 100)
gjetning = hemmelig_tall + 1  # Initialiserer løkka

gjett = 0
while gjetning != hemmelig_tall:
    gjetning = spør_gjetning()
    gjett += 1
    tilbakemelding(gjetning)
