"""
Wrapper around geopy library
"""
import json
import logging
import os

from geopy import distance

PATH = os.path.dirname(os.path.realpath(__file__))
PLACE_NAMES = ["atms", "gas_stations", "restaurants", "stations", "supermarkets"]


class Map:
    """Represent a map obj."""

    def __init__(self, lat, lon):
        """Initialize the map objects."""
        self.center = (lat, lon)
        self.places = dict()

    def add_places(self, place_name):
        """Read place data from file and store in memory."""
        if place_name not in PLACE_NAMES:
            raise "check the palce name"
        data_file = open(PATH + "/static/data/berlin_%s.json" % place_name).read()
        places = json.loads(data_file)
        for place in places:
            self.places.update({place.get("id"): place})

    def meters(self, lat, lon):
        """Return the distance between two points in meters."""
        dist = distance.distance(self.center, (lat, lon)).meters
        return round(float(dist), 2)

    def get_sorted_places(self, max_dist):
        """Return a list of tuples id/distance sorted by distance."""
        ids_dists = dict()
        for place_id, place in self.places.items():
            dist = self.meters(place.get("lat"), place.get("lon"))
            if dist > max_dist:
                continue
            ids_dists.update({place_id: dist})
            place.update({"distance": dist})
        sorted_list = sorted(ids_dists.items(), key=lambda item: item[1])
        return sorted_list

    def closest(self, amount, max_dist):
        """Return the distance between two points in meters."""
        sorted_list = self.get_sorted_places(max_dist)
        place_ids = list(item[0] for item in sorted_list[:amount])
        places = list(self.places[place_id] for place_id in place_ids)
        return places


def get_closest_restaurants(lat, lon):
    """Return the 10 or less closest restaurant from the given lat/lon."""
    my_map = Map(lat, lon)
    my_map.add_places("restaurants")
    closest_items = my_map.closest(10, 10000)
    logging.debug(closest_items)
    return closest_items
