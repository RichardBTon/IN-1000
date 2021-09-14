class Person:
    def __init__(self, alder, kjønn, sivilstatus, gjeld):
        # Har noen tester for om det er korrekt info, men orker ikke lage alt så omfattende.
        self.alder = int(alder)

        # Sjekker om det er et godtatt kjønn. Kan hende man burde fått en errormelding og ikke fått lov til å lage klassen, men jeg nøyer meg med å sette kjønn til None
        kjønn = kjønn.lower()
        if kjønn in ["mann", "kvinne", None]:
            self.kjønn = kjønn

        else:
            self.sivilstatus = None
            print("Kjønn ikke i liste.")

        # Sjekker om det er en godtatt sivilstatus. Kan hende man burde fått en errormelding og ikke fått lov til å lage klassen, men jeg nøyer meg med å sette sivilstatus til None
        sivilstatus = sivilstatus.lower()
        if sivilstatus in ["gift", "singel", None]:
            self.sivilstatus = sivilstatus

        else:
            self.sivilstatus = None
            print("Sivilstatus ikke i liste.")

        self.gjeld = float(gjeld)

    def print_info(self):
        print(
            f"Du er en {self.sivilstatus} {self.kjønn} på {self.alder} år med {self.gjeld} kr i gjeld.")

    def vil_betale(self):
        # Enkelt prediksjonsprogram
        # Kunne nok delt opp if-setningene i mann og kvinne for å gjøre det mer oversiktlig og unngå repitisjon.
        vil_betale = True

        if self.kjønn == "mann" and self.alder < 30 and self.sivilstatus == "singel" and self.gjeld > 100000:
            vil_betale = False

        elif self.kjønn == "mann" and self.alder < 25 and self.gjeld > 200000:
            vil_betale = False

        elif self.kjønn == "kvinne" and self.alder < 28 and self.sivilstatus == "singel" and self.gjeld > 200000:
            vil_betale = False

        return vil_betale


def create_person():
    # Gjør ikke dette i __init__ i selve klassen fordi man sannsynligvis vil ha informasjonen fra et annet sted i framtiden
    alder = int(input("Skriv inn alderen din: "))
    kjønn = input("Skriv inn om du er mann eller kvinne: ")
    sivilstatus = input("Skriv inn om du er gift eller singel: ")
    gjeld = float(input("Skriv inn gjelden din: "))

    return Person(alder, kjønn, sivilstatus, gjeld)


def main():
    eksempel = create_person()
    eksempel.print_info()

    vil_betale = "Vil betale." if eksempel.vil_betale() else "Vil ikke betale."
    print(vil_betale)


if __name__ == "__main__":
    main()
