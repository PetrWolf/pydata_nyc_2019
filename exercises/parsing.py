# Utilities for data cleaning
import os

def parse_location(location):
    """Extracts latitude and longitude from a location string.

    Args:
        location: Decimal Degrees (D.D) representation of a geographical location, 
            e.g. "34.56 N 123.45 W"
    
    Returns:
        latitude, longitude
    """
    latitude_str, north_south, longitude_str, east_west = location.split()
    latitude = float(latitude_str) * -1 if north_south == "S" else 1
    longitude = float(longitude_str) * -1 if east_west == "W" else -1

    return latitude, longitude_str
