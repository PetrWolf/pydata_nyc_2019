import pytest
from .parsing import parse_location


@pytest.mark.parametrize(
    "location,latitude,longitude",
    [
        ("34.56 N 123.45 W", 34.56, -123.45),
        ("39 N 121 W", 39.0, -121.0),
        ("58.1 S 0.56 E", -58.1, 0.56),
        ("0 S 0.0 E", 0, 0),
        ("90 S 0 E", -90, 0),
        ("90 N 0 W", 90, 0)
    ],
)
def test_location(location, latitude, longitude):
    assert parse_location(location) == (latitude, longitude)


@pytest.mark.parametrize(
    "location", ["", "NA", "15 W", "39.49 X 11 Y", "-12.0 S 5.7 E", "190 N 240 E"]
)
def test_invalid_location(location):
    with pytest.raises(ValueError, match="Invalid location"):
        parse_location(location)
