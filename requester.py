"""Main endpoints module."""
from urllib.parse import urlencode

import requests


def get_latlon_from_address(address):
    """Submit a request to nominatim and return the lat/lon of first result."""
    querystring = {"format": "json"}
    params = urlencode(querystring)
    url = "https://nominatim.openstreetmap.org/search/%s?%s" % (address, params)
    req = requests.get(url)
    data = req.json()
    if not data:
        return None, None
    place = data[0]
    lat, lon = place["lat"], place["lon"]
    return lat, lon
