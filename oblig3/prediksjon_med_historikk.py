class Person:
    def __init__(self, alder, kjønn, sivilstatus, gjeld, utdanning, historikk):
        # Har noen tester for om det er korrekt info, men orker ikke lage alt så omfattende.
        self.alder = int(alder)

        kjønn = kjønn.lower()
        if kjønn in ["mann", "kvinne"]:
            self.kjønn = kjønn

        else:
            raise ValueError("Kjønn ikke i liste.")

        sivilstatus = sivilstatus.lower()
        if sivilstatus in ["gift", "singel"]:
            self.sivilstatus = sivilstatus

        else:
            raise ValueError("Sivilstatus ikke i liste.")

        self.gjeld = float(gjeld)

        self.historikk = historikk

        # Kunne sjekket om "in" en godkjent liste som tidligere, men gidder ikke
        self.utdanning = utdanning

        self.inntekt_for_utdanning = {
            "ukjent": 300000,
            "grunnskole": 260000,
            "hoeyskole": 5000000,
            "universitet": 700000,
        }

    def print_info(self):
        print(
            f"Du er en {self.sivilstatus} {self.kjønn} på {self.alder} år med {self.gjeld} kr i gjeld.")

    def vil_betale(self):
        # Prediksjonsprogram
        vil_betale = True

        if self.kjønn == "mann":
            if self.inntekt_for_utdanning[self.utdanning] * 3 > self.gjeld:
                # Sjekker ikke videre
                return True

            elif self.alder < 30 and self.sivilstatus == "singel" and self.gjeld > 100000:
                vil_betale = False

            elif self.alder < 25 and self.gjeld > 200000:
                vil_betale = False

        elif self.kjønn == "kvinne" and self.alder < 28 and self.sivilstatus == "singel" and self.gjeld > 200000:
            vil_betale = False

        # Sjekk for historikk
        ikke_betalt = 0
        for betalt in self.historikk:
            if not betalt:
                ikke_betalt += 1

        if ikke_betalt >= 2:
            vil_betale = False

        return vil_betale


def input_historikk():
    historikk = []

    for i in range(3):
        betalt_str = input(
            f"Skriv betalt hvis betalt for {i +1} måned siden, og ikke_betalt hvis ikke: ")

        # Sjekk om godkjent input
        while betalt_str not in ["betalt", "ikke_betalt"]:
            print("Ikke et av alternativene")
            betalt_str = input(
                f"Skriv betalt hvis betalt for {i +1} måned siden, og ikke_betalt hvis ikke: ")

        betalt = True if betalt_str == "betalt" else False
        historikk.append(betalt)

    print(f"historikk: {historikk}")
    return historikk


def create_person():
    # Gjør ikke dette i __init__ i selve klassen fordi man sannsynligvis vil ha informasjonen fra et annet sted i framtiden

    # alder = int(input("Skriv inn alderen din: "))
    # kjønn = input("Skriv inn om du er mann eller kvinne: ")
    # sivilstatus = input("Skriv inn om du er gift eller singel: ")
    # gjeld = float(input("Skriv inn gjelden din: "))
    # utdanning = input(
    #     "Skriv inn ditt utdanningsnivå (ukjent, grunnskole, hoeyskole eller universitet): ")
    # historikk = input_historikk()

    # Eksempler for å unngå input under testing:

    alder = 21
    kjønn = "mann"
    sivilstatus = "gift"
    gjeld = 3000000
    utdanning = "universitet"
    historikk = [True, False, False]

    return Person(alder, kjønn, sivilstatus, gjeld, utdanning, historikk)


def main():
    eksempel = create_person()
    eksempel.print_info()

    vil_betale = "Vil betale." if eksempel.vil_betale() else "Vil ikke betale."
    print(vil_betale)


if __name__ == "__main__":
    main()
