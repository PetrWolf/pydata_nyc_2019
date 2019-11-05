from .parsing import parse_location

def test_location():
    assert parse_location("34.56 N 123.45 W") == (34.56, -123.45)
