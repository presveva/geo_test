"""
Module combo find and return pairs of restaurants (maximum 10 pairs)
that are close to each other.
"""
import json
import os
import time

from geopy import distance

PATH = os.path.dirname(os.path.realpath(__file__))


def get_closest_pairs(cousine_a, cousine_b):
    restaurants_a, restaurants_b = restaurant_pairs(cousine_a, cousine_b)
    closest_pairs = list()
    for restaurant_a in restaurants_a:
        lower_dist, restaurant_b = get_restaurant_b(restaurant_a, restaurants_b)
        closest_pairs.append(
            {"cousine_a": restaurant_a, "cousine_b": restaurant_b, "dist": lower_dist}
        )
    sorted_list = sorted(closest_pairs, key=lambda item: item["dist"])[:10]
    return sorted_list


def get_restaurant_b(restaurant_a, restaurants_b):
    lat_a, lon_a = restaurant_a.get("lat"), restaurant_a.get("lon")
    lower_dist, closer = None, None
    for restaurant_b in restaurants_b:
        lat_b, lon_b = restaurant_b.get("lat"), restaurant_b.get("lon")
        dist = meters(lat_a, lon_a, lat_b, lon_b)
        if lower_dist is None or dist < lower_dist:
            lower_dist = dist
            closer = restaurant_b
    # print(restaurant_a.get("id"), closer.get("id"), lower_dist)
    return lower_dist, closer


def meters(lat1, lon1, lat2, lon2):
    """Return the distance between two points in meters."""
    dist = distance.distance((lat1, lon1), (lat2, lon2)).meters
    return round(float(dist), 2)


def restaurant_pairs(cousine_a, cousine_b):
    """Read place data from file and store in memory."""
    restaurants_a, restaurants_b = list(), list()
    data_file = open(PATH + "/static/data/berlin_restaurants.json").read()
    restaurants = json.loads(data_file)
    for restaurant in restaurants:
        cuisine = restaurant.get("tags", {}).get("cuisine", None)
        if cuisine == cousine_a:
            restaurants_a.append(restaurant)
        if cuisine == cousine_b:
            restaurants_b.append(restaurant)
    if len(restaurants_a) > len(restaurants_b):
        return restaurants_b, restaurants_a
    return restaurants_a, restaurants_b


if __name__ == "__main__":
    start_time = time.time()
    # pair = get_closest_pairs("italian", "vietnamese")
    pair = get_closest_pairs("vietnamese", "italian")
    print("--- %s seconds ---" % (time.time() - start_time))
