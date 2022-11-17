from dashboard.tweet_analysis import parse_tweet_input


def test_parsing():
    assert parse_tweet_input(
        'https://twitter.com/lecartographe/status/1592765408754311168?s=20&t=Ib1_Q7lD7IMtmZVQUAkFQQ') == 1592765408754311168
    assert parse_tweet_input('1592765408754311168') == 1592765408754311168
