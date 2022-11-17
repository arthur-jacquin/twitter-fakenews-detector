from dashboard.utils import barycentre, force_0_1


def test_force_0_1():
    assert force_0_1(-.2) == 0
    assert force_0_1(.5) == .5
    assert force_0_1(1.3) == 1


def test_barycentre():
    assert barycentre([(0, 1), (1, 3)]) == .75
