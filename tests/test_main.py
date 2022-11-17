from main import update_output_topic, update_output_user, update_output_tweet


def test_main():
    assert update_output_topic(1, 'trump', 1) != None
    assert update_output_user(1, 'elonmusk') != None
    assert update_output_tweet(1, '1592765408754311168') != None
