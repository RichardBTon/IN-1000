class Stein():
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
