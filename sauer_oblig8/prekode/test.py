from spillbrett import Spillbrett
from sau import Sau
from gress import Gress
from sauehjerne import vanligste_element


def test_avstand():
    spillbrett = Spillbrett(3000)
    sau = Sau("sau2", 400, 500, spillbrett)
    gress = Gress("gress", 100, 100)

    assert sau._sauehjerne.avstand_til_objekt(gress) == 14, "Avstanden er feil"
    print("Avstandstest ferdig")


def test_retning():
    spillbrett = Spillbrett(3000)
    sau = Sau("sau2", 400, 500, spillbrett)
    gress = Gress("gress", 100, 100)
    retninger_mot = sau.sauehjerne().retninger_mot_objekt(gress)
    assert set(retninger_mot) == set(
        ["opp", "venstre"]), "Retninger_mot er feil"
    retninger_fra = sau.sauehjerne().retninger_fra_objekt(gress)
    assert set(retninger_fra) == set(["ned", "høyre"]), "Retninger_fra er feil"
    print("Retningstest ferdig")


def test_vanligste_element():
    assert vanligste_element(["ned", "ned", "opp"]) == "ned"
    assert vanligste_element(["ned", "venstre", "opp", "venstre"]) == "venstre"
    assert vanligste_element(
        ["ned", "ned", "opp", "venstre", "opp", "opp", "ned", "ned"]) == "ned"
    print("Test vanligste element ferdig")


test_retning()
