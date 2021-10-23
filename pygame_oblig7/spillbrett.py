from sau import Sau


class Spillbrett():
    def __init__(self):
        self._sauer = []

    def opprett_sau(self, x, y, bilde):
        ny_sau = Sau(x, y, bilde)
        self.sauer.append(ny_sau)

    def oppdater(self):
        for sau in self.sauer:
            sau.beveg()
