# from pgzero import *

# Syntes det var veldig lange navn med posisjon_venstre og posisjon_topp, og x og y er vel så informativt, så endra det.


class Sau():
    def __init__(self, x, y, bilde):
        self.x = x
        self.y = y
        self.bilde = bilde

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

    # Bevegelse

    def beveg(self):
        self.x += self.vx
        self.y += self.vy

    def snu(self):
        self.vx = - self.vx
        self.vy = - self.vy

    def skjerm():
        pass

    def tegn(self, skjerm):
        skjerm.blit(self.bilde, (self.x, self.y))
