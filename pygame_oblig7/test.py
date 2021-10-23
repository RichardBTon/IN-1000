from sau import Sau
from spillbrett import Spillbrett
from ulv import Ulv


def sau_test():
    testsau = Sau(50, 50, "sau")
    testsau.set_pos(0, 0)
    testsau.set_vx(10)
    testsau.set_vy(20)

    testsau.beveg()
    testsau.beveg()

    assert testsau.get_x() == 20
    assert testsau.get_y() == 40

    testsau.snu()

    assert testsau.get_vx() == -10
    assert testsau.get_vy() == -20

    testsau.beveg()

    assert testsau.get_x() == 10
    assert testsau.get_y() == 20

    print("Testing av sau ferdig")


def test_finn_naermeste_sau():
    brett = Spillbrett()
    brett.opprett_sau(0, 0, "sau")
    brett.opprett_sau(100, 100, "sau",)
    ulv = brett.opprett_ulv(90, 80, "ulv")
    naermeste_sau = ulv.finn_nærmeste_sau()
    # Det bør printes 100, 100, ettersom denne sauen er nærmest ulven
    print(naermeste_sau.get_x(),
          naermeste_sau.get_y())


test_finn_naermeste_sau()
