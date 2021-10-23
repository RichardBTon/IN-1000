from sau import Sau


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


sau_test()
