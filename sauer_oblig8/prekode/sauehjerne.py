# from stein import Stein
from random import randint


def motsatt_retning(retning):
    if retning == "venstre":
        motsatt = "hoeyre"
    elif retning == "hoeyre":
        motsatt = "venstre"
    elif retning == "opp":
        motsatt = "ned"
    elif retning == "ned":
        motsatt = "opp"
    else:
        raise TypeError(f"{retning} er ikke en godkjent retning")

    return motsatt


def vanligste_element(liste):
    # Kan bruke count, men kanskje juks?
    # Det finnes sikkert raskere metoder, men siden jeg vet at det aldri er mer enn 4 forskjellige elementer, er det ikke så farlig...
    if not liste:
        return
    forskjellige_elementer = []
    for element in liste:
        nytt_element = True
        for i, forskjellig_element in enumerate(forskjellige_elementer):
            if element == forskjellig_element["element"]:
                nytt_element = False
                elementindex = i  # Kunne sikkert bare brukt i direkte senere, men det er lite ryddig
                break  # Kanskje ikke nødvendig, men tar ingen sjanser
        if nytt_element:
            forskjellige_elementer.append({
                "element": element,
                "antall": 1
            })
        else:
            forskjellige_elementer[elementindex]["antall"] += 1

    høyest_antall = forskjellige_elementer[0]
    for forskjellig_element in forskjellige_elementer:
        if forskjellig_element["antall"] > høyest_antall["antall"]:
            høyest_antall = forskjellig_element

    return høyest_antall["element"]


class Sauehjerne:
    def __init__(self, sau, spillbrett):
        self._sau = sau
        self._spillbrett = spillbrett

    def velg_retning(self):
        nærmeste_gress = self.finn_nærmeste_gress()

        retninger = []
        if nærmeste_gress is not None:
            retninger.extend(self.retninger_mot_objekt(nærmeste_gress))

        ulv = self._spillbrett.ulv()
        if self.avstand_til_objekt(ulv) < 6:
            retninger_fra_ulv = self.retninger_fra_objekt(ulv)
            retninger.extend(retninger_fra_ulv * 2)

        valgt_retning = vanligste_element(retninger)

        if valgt_retning == None:
            print("============ Ferdig ============")
            print("Sauen har vunnet, det feires med en TypeError!")

        # Sauen følger kanten av brettet
        if self._sau.rute_venstre() == 17 and valgt_retning == "hoeyre":
            valgt_retning = "ned"
        elif self._sau.rute_topp() == 0 and valgt_retning == "opp":
            valgt_retning = "hoeyre"
        elif self._sau.rute_venstre() == 0 and valgt_retning == "venstre":
            valgt_retning = "opp"
        elif self._sau.rute_topp() == 13 and valgt_retning == "ned":
            valgt_retning = "venstre"

        retninger = ["hoeyre", "venstre", "opp", "ned"]
        if self.stein_finnes_i_retning(valgt_retning):
            retninger.remove(valgt_retning)
            retning = retninger[randint(0, len(retninger)-1)]
            while self.hinder_finnes_i_retning(retning):
                retning = retninger[randint(0, len(retninger)-1)]
            else:
                valgt_retning = retning

        return valgt_retning

    def avstand_til_objekt(self, objekt):
        avstand_venstre = abs(objekt.rute_venstre() - self._sau.rute_venstre())
        avstand_topp = abs(objekt.rute_topp() - self._sau.rute_topp())

        return avstand_venstre + avstand_topp

    def retninger_mot_objekt(self, objekt):
        retninger = []

        avstand_venstre = int(objekt.rute_venstre() - self._sau.rute_venstre())
        avstand_topp = int(objekt.rute_topp() - self._sau.rute_topp())

        if avstand_venstre < 0:
            retning_x = "venstre"
        elif avstand_venstre > 0:
            retning_x = "hoeyre"
        else:
            retning_x = None

        if avstand_topp < 0:
            retning_y = "opp"
        elif avstand_topp > 0:
            retning_y = "ned"
        else:
            retning_y = None

        # Usikker på om jeg skal ha det sånn, eller at den bare gir en retning y, og en x.
        # Nå vil jo dette føre til at sauen har mer lyst til å bevege seg mot gresset jo lenger unna det er, men kanskje det er realistisk fordi sauen blir sulten?
        # if retning_y is not None:
        #     for i in range(abs(avstand_topp)):
        #         retninger.append(retning_y)
        # if retning_x is not None:
        #     for i in range(abs(avstand_venstre)):
        #         retninger.append(retning_x)

        # Men dette er nok bedre, for det gir jo mening at å ikke bli spist burde ha 1. prioritet...
        if retning_x is not None:
            retninger.append(retning_x)
        if retning_y is not None:
            retninger.append(retning_y)

        return retninger

    def retninger_fra_objekt(self, objekt):
        retninger_mot = self.retninger_mot_objekt(objekt)
        retninger_fra = []

        for retning_mot in retninger_mot:
            retning_fra = motsatt_retning(retning_mot)
            retninger_fra.append(retning_fra)

        return retninger_fra

    def finn_nærmeste_gress(self):
        nærmest = None
        for gress in self._spillbrett.gress():
            if not gress.er_spist():
                avstand = self.avstand_til_objekt(gress)
                if nærmest is None:
                    nærmest = {
                        "gress": gress,
                        "avstand": avstand
                    }
                elif nærmest["avstand"] > avstand:
                    nærmest = {
                        "gress": gress,
                        "avstand": avstand
                    }
                else:
                    pass
        if nærmest is None:
            return nærmest
        else:
            return nærmest["gress"]

    def rute_i_retning(self, retning):
        # Kanskje litt sært å kalle det for v, men usikker på hva annet som passer som ikke er dritlangt
        vx = 0
        vy = 0
        if retning == "hoeyre":
            vx = 1
        elif retning == "venstre":
            vx = -1
        elif retning == "opp":
            vy = -1
        elif retning == "ned":
            vy = 1
        else:
            raise TypeError(f"{retning} er ikke en godkjent retning")

        sjekk_y = self._sau.rute_topp() + vy
        sjekk_x = self._sau.rute_venstre() + vx

        return (sjekk_x, sjekk_y)

    def stein_finnes_i_retning(self, retning):

        sjekk_x, sjekk_y = self.rute_i_retning(retning)
        # Føles som man med spillbrett burde kunne sjekke dette direkte bare med koordinatene, men det går vel ikke...
        stein_i_retning = False
        for stein in self._spillbrett.steiner():
            if stein.rute_topp() == sjekk_y and stein.rute_venstre() == sjekk_x:
                stein_i_retning = True
        return stein_i_retning

    def hinder_finnes_i_retning(self, retning):

        if self.stein_finnes_i_retning(retning):
            return True

        sjekk_x, sjekk_y = self.rute_i_retning(retning)

        if 0 > sjekk_x or sjekk_x > 18:
            return True

        elif 0 > sjekk_y or sjekk_y > 13:
            return True
        return False
