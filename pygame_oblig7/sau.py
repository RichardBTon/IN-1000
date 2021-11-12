# Syntes det var veldig lange navn med posisjon_venstre og posisjon_topp, og x og y er vel så informativt, så endra det.

from random import randint


class Sau():
    def __init__(self, x, y, bilde):
        self.x = x
        self.y = y
        self.bilde = bilde

        self.vx = 1
        self.vy = 1

        self.spist = False

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

    # Spising

    def blir_spist(self):
        self.spist = True

    def er_spist(self):
        return self.spist

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
        # Fordi fart kan være 2 blir den stuck i veggen innimellom

        if randint(1, 1000) < 9:
            self.set_vx_og_vy(randint(-2, 2), randint(-2, 2))

        if randint(1, 1000) < 5:
            if -2 <= self.get_vx() <= 2 and -2 <= self.get_vy() <= 2:
                ny_vx = self.get_vx() + 1
                ny_vy = self.get_vy() - 1
                self.set_vx_og_vy(ny_vx, ny_vy)

            else:
                self.set_vx_og_vy(randint(-2, 2), randint(-2, 2))

        if randint(1, 1000) < 5:
            if -2 <= self.get_vx() <= 2 and -2 <= self.get_vy() <= 2:
                ny_vx = self.get_vx() - 1
                ny_vy = self.get_vy() + 1
                self.set_vx_og_vy(ny_vx, ny_vy)
            else:
                self.set_vx_og_vy(randint(-2, 2), randint(-2, 2))

    def snu(self):
        self.vx = - self.vx
        self.vy = - self.vy

    def skjerm():
        pass

    def tegn(self, skjerm):
        skjerm.blit(self.bilde, (self.x, self.y))
