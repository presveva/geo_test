"""Main endpoints module."""
# import logging

from flask import Flask, jsonify, redirect, render_template

import distance
import requester
import combo

app = Flask(__name__)


@app.route("/")
def home():
    """Display a map which contains all the markers in data."""
    return redirect("/cluster")


@app.route("/cluster")
def cluster():
    """Display a map which contains all the markers in data."""
    return render_template("cluster.html", app="unrealists", page="cluster")


@app.route("/restaurants/near/<lat>/<lon>")
def restaurants_near_latlon(lat, lon):
    """Return the closest restaurants from the given lat/lon."""
    closest_items = distance.get_closest_restaurants(lat, lon)
    return jsonify(closest_items)


@app.route("/restaurants/near/<address>")
def restaurants_near_address(address):
    """Return the closest restaurants from the given address."""
    lat, lon = requester.get_latlon_from_address(address)
    if not lat:
        return jsonify({"error": "no address in nominatim"})
    closest_items = distance.get_closest_restaurants(lat, lon)
    return jsonify(closest_items)


@app.route("/restaurants/combo/<cuisine_a>/<cuisine_b>")
def restaurants_combo(cuisine_a, cuisine_b):
    """Return the closest pair of restaurants by the given cuisines."""
    closest_restaurants = combo.get_closest_pairs(cuisine_a, cuisine_b)
    return jsonify(closest_restaurants)
