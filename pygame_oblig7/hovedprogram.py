# from pgzero import *
import pgzrun
from spillbrett import Spillbrett
# Her lager vi et nytt spillbrett og oppretter to sauer med ulike bilder og ulike start-posisjoner
spillbrett = Spillbrett()
spillbrett.opprett_sau(100, 100, "sau")
spillbrett.opprett_sau(400, 400, "sau2")


# Dette er prekode som gjør at pygame zero fungerer. Ikke endre dette:
WIDTH = 900
HEIGHT = 700


def draw():
    screen.fill((128, 81, 9))
    spillbrett.tegn(screen)


def update():
    spillbrett.oppdater()


pgzrun.go()
