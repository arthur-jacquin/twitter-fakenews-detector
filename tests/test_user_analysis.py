from dashboard.user_analysis import parse_user_input


def test_parsing():
    assert parse_user_input(
        'https://twitter.com/lecartographe') == 'lecartographe'
    assert parse_user_input('lecartographe') == 'lecartographe'
