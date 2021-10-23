from sau import Sau
from gress import Gress
from stein import Stein
from ulv import Ulv


class Spillbrett():
    def __init__(self):
        self._sauer = []
        self._gress = []

        self._steiner = []
        self._ulver = []

    # Getters
    def get_ulver(self):
        return self._ulver

    def get_steiner(self):
        return self._steiner

    def get_sauer(self):
        return self._sauer

    def get_gress(self):
        return self._gress

    # Setters?

    def opprett_sau(self, x, y, bilde):
        ny_sau = Sau(x, y, bilde)
        self._sauer.append(ny_sau)
        return ny_sau

    def opprett_gress(self, x, y, bilde):
        nytt_gress = Gress(x, y, bilde)
        self._gress.append(nytt_gress)
        return nytt_gress

    def opprett_ulv(self, x, y, bilde):
        ny_ulv = Ulv(x, y, bilde, self)
        self._ulver.append(ny_ulv)
        return ny_ulv

    def opprett_stein(self, x, y, bilde):
        ny_stein = Stein(x, y, bilde)
        self._steiner.append(ny_stein)
        return ny_stein

    def oppdater(self):
        for sau in self._sauer:
            sau.beveg()

        for ulv in self._ulver:
            ulv.beveg()

    def tegn(self, skjerm):
        for sau in self._sauer:
            sau.tegn(skjerm)

        for gress in self._gress:
            gress.tegn(skjerm)

        for ulv in self._ulver:
            ulv.tegn(skjerm)

        for stein in self._steiner:
            stein.tegn(skjerm)
