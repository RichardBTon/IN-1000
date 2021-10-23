# Syntes det var veldig lange navn med posisjon_venstre og posisjon_topp, og x og y er vel så informativt, så endra det.

from random import randint
import math


def regn_avstand(pos1, pos2):
    """pos1 og pos2 skal være koordinater i tuples eller lister"""
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return math.sqrt(dx * dx + dy * dy)


class Ulv():
    def __init__(self, x, y, bilde, spillbrett):
        self.x = x
        self.y = y
        self.bilde = bilde

        self.sauer = spillbrett.get_sauer()
        self.steiner = spillbrett.get_steiner()

        self.vx = 1
        self.vy = 1

    # Getters

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    # Setters

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_vx(self, vx):
        self.vx = vx

    def set_vy(self, vy):
        self.vy = vy

    def set_vx_og_vy(self, vx, vy):
        self.vx = vx
        self.vy = vy

    # Bevegelse

    def beveg(self):
        screen_size_x = 900
        screen_size_y = 700
        self.x += self.vx
        self.y += self.vy

        # Veggkollisjon
        if self.x + 50 >= screen_size_x or self.x <= 0:
            self.snu()

        elif self.y + 50 >= screen_size_y or self.y <= 0:
            self.snu()

        # Tilfeldig bevegelse, kan sikkert lage dette mer modulært, men går fint nå

        if randint(1, 1000) < 7:
            self.set_vx_og_vy(randint(-3, 3), randint(-3, 3))

        if randint(1, 1000) < 2:
            if -5 <= self.get_vx() <= 5 and -5 <= self.get_vy() <= 5:
                ny_vx = self.get_vx() + 1
                ny_vy = self.get_vy() - 2
                self.set_vx_og_vy(ny_vx, ny_vy)

            else:
                self.set_vx_og_vy(randint(-2, 2), randint(-2, 2))

        if randint(1, 1000) < 2:
            if -5 <= self.get_vx() <= 5 and -5 <= self.get_vy() <= 5:
                ny_vx = self.get_vx() - 2
                ny_vy = self.get_vy() + 1
                self.set_vx_og_vy(ny_vx, ny_vy)
            else:
                self.set_vx_og_vy(randint(-2, 2), randint(-2, 2))

    def finn_nærmeste_sau(self):
        første_sau = self.sauer[0]
        selfpos = (self.x, self.y)
        nærmest = {
            "sau": første_sau,
            "avstand": regn_avstand(selfpos, (første_sau.x, første_sau.y))
        }
        for sau in self.sauer:
            avstand = regn_avstand(selfpos, (sau.x, sau.y))

            if avstand < nærmest["avstand"]:
                nærmest = {
                    "sau": sau,
                    "avstand": avstand
                }

        return nærmest["sau"]

    def snu(self):
        self.vx = - self.vx
        self.vy = - self.vy

    def skjerm():
        pass

    def tegn(self, skjerm):
        skjerm.blit(self.bilde, (self.x, self.y))
