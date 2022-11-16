from ML.vectorisation import vectorisation, vectorisation_df


def test_vectorisation():
    assert vectorisation('EmManuel, MACroN%') == ['emmanuel macron']


def test_vectorisation_df():
    assert vectorisation_df(['EmManuel, MACroN%', 'bIDen']) == [
        'emmanuel macron', 'biden']
