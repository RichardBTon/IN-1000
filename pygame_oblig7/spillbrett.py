from sau import Sau


class Spillbrett():
    def __init__(self):
        self._sauer = []

    def opprett_sau(self, x, y, bilde):
        ny_sau = Sau(x, y, bilde)
        self._sauer.append(ny_sau)

    def oppdater(self):
        for sau in self._sauer:
            sau.beveg()

    def tegn(self, skjerm):
        for sau in self._sauer:
            sau.tegn(skjerm)
