from dashboard.utils import to_li_item, barycentre, force_0_1, format_age, format_activity


def test_to_li_item():
    assert to_li_item('li name') != None


def test_force_0_1():
    assert force_0_1(-.2) == 0
    assert force_0_1(.5) == .5
    assert force_0_1(1.3) == 1


def test_barycentre():
    assert barycentre([(0, 1), (1, 3)]) == .75


def test_format_age():
    assert format_age(13.5*3600) == '13 hour(s)'
    assert format_age(2.5*3600*24*365) == '2 year(s)'


def test_format_activity():
    assert format_activity(2.5/(24*3600)) == '2 status(es) per day'
    assert format_activity(1/(2*365*24*3600)) == 'Less than once a year'
