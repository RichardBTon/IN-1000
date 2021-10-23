# Hadde det ikke vært bedre å ha én basic klasse med setters og getters for så å bruke super?
# Hadde jo sett litt penere ut og vært mer modulært hvis man ville endra noe basic

class Gress():
    def __init__(self, x, y, bilde):
        self.x = x
        self.y = y
        self.bilde = bilde

        self.spist = False

    # Getters

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Setters

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    # Spising

    def blir_spist(self):
        self.spist = True

    def er_spist(self):
        return self.spist
    # Pygame zero

    def skjerm():
        pass

    def tegn(self, skjerm):
        skjerm.blit(self.bilde, (self.x, self.y))
