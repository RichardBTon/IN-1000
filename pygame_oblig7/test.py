from sau import Sau
from gress import Gress
from stein import Stein
from ulv import Ulv

from spillbrett import Spillbrett
from spillbrett import har_kollidert


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


def test_har_kollidert():
    brett = Spillbrett()
    # Test-case 1: Disse to objektene har kollidert, fordi ulven ligger delvis oppå sauen
    sau = Sau(50, 50, "sau")
    ulv = Ulv(60, 60, "ulv", brett)
    assert har_kollidert(sau, ulv)
    # Rekkefølgen skal ikke ha noe å si
    assert har_kollidert(ulv, sau)

    # Test-case 2: Disse to objektene ligger rett ved siden av hverandre
    # og har ikke kollidert (husk at de er 50px brede/høye):
    gress = Gress(100, 100, "gress")
    sau = Sau(150, 150, "sau",)
    assert not har_kollidert(gress, sau)

    # Test-case 3: Disse har kollidert
    stein = Stein(100, 100, "gress")
    ulv = Ulv(120, 110, "sau", brett)
    assert har_kollidert(stein, ulv)

    # Test-case 4: Disse har kollidert
    sau = Sau(400, 200, "sau")
    stein = Stein(449, 230, "stein")
    assert har_kollidert(sau, stein)

    print("test_har_kollidert fullført.")


test_har_kollidert()
