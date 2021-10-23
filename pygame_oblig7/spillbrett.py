from sau import Sau
from gress import Gress


class Spillbrett():
    def __init__(self):
        self._sauer = []
        self._gress = []

    def opprett_sau(self, x, y, bilde):
        ny_sau = Sau(x, y, bilde)
        self._sauer.append(ny_sau)

    def opprett_gress(self, x, y, bilde):
        nytt_gress = Gress(x, y, bilde)
        self._gress.append(nytt_gress)

    def oppdater(self):
        for sau in self._sauer:
            sau.beveg()

    def tegn(self, skjerm):
        for sau in self._sauer:
            sau.tegn(skjerm)
        for gress in self._gress:
            gress.tegn(skjerm)
