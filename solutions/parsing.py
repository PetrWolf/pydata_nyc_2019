"""Utilities for data cleaning"""

from typing import Tuple
import re

LOCATION_RE = re.compile(r"^([0-9]+(?:\.[0-9]+)?) ([NS]) ([0-9]+(?:\.[0-9]+)?) ([EW])$")


def parse_location(location: str) -> Tuple[float, float]:
    """Extracts latitude and longitude from a given location string.

    Args:
        location: Decimal Degrees (D.D) representation of a geographical location,
            e.g. "34.56 N 123.45 W"

    Returns:
        latitude, longitude

    Raises:
        ValueError: for invalid locations

    Example:
        >>> parse_location("34.56 N 123.45 W")
        (34.56, -123.45)

        >>> parse_location("nowhere")
        Traceback (most recent call last):
            ...
        ValueError: Invalid location "nowhere"
    """
    match = LOCATION_RE.match(location)

    if match:
        latitude_str, north_south, longitude_str, east_west = match.groups()
        latitude, longitude = float(latitude_str), float(longitude_str)

        if (0 <= latitude <= 90) and (0 <= longitude <= 180):
            return (
                latitude * (-1 if north_south == "S" else 1),
                longitude * (-1 if east_west == "W" else 1),
            )

    raise ValueError(f'Invalid location "{location}"')
