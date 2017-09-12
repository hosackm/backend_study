from collections import namedtuple
from urllib.parse import urlencode
import requests

Coordinate = namedtuple("Coordinate", ["lat", "lng"])

FOURSQUARE_CLIENT_ID = "432UR1ROVWNLP0G3LU2SF3QOKZQ53XL0411G5IP3CZUQFRDO"
FOURSQUARE_CLIENT_SECRET = "1ROWRVOGF11U5FIZZLNXPYT2WP0CF3RH1M3GGIUPL2XID4XW"
GOOGLE_API_KEY = "AIzaSyBF647CLJc5t2gX2iR7QPvebfuavGDJnfo"
FOURSQUARE_BASE_URL = "https://api.foursquare.com/v2/venues/search"
GOOGLE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"


def build_url(base, **kwargs):
    """
    Returns a URL with all the keyword arguments as URL query parameters
    """
    return base + "?" + urlencode(kwargs)


def get_coordinate(location):
    """
    Do a Google Geolocation API lookup of the location as a string
    """
    parameters = {
        "address": location,
        "key": GOOGLE_API_KEY,
    }
    search_url = build_url(GOOGLE_BASE_URL, **parameters)

    response = requests.get(search_url)
    latlong = response.json()["results"][0]["geometry"]["location"]
    return Coordinate(**latlong)


def search_foursquare(query_string, coordinate):
    """
    Do a search of query_string in the latitude and longitude in coordinate
    """
    parameters = {
        "query": query_string,
        "ll": "{},{}".format(*coordinate),
        "client_id": FOURSQUARE_CLIENT_ID,
        "client_secret": FOURSQUARE_CLIENT_SECRET,
        "v": "20170905",
        "limit": "5"
    }
    search_url = build_url(FOURSQUARE_BASE_URL, **parameters)
    response = requests.get(search_url)
    return response.json()["response"]["venues"][0]


def lookup_meal(location, meal_type):
    """
    Lookup a meal in the provided location. This is a mashup function for combining Google Geolocation
    and Foursquare search APIs
    """
    coord = get_coordinate(location)
    restaurant_info = search_foursquare(meal_type, coord)

    return {
        "name": restaurant_info.get("name"),
        "address": " ".join(restaurant_info.get("location").get("formattedAddress")),
        "image": "512".join(restaurant_info.get("categories")[0]["icon"].values())
    }


if __name__ == "__main__":
    from pprint import pprint
    coord = get_coordinate("2905 Harrison Street San Francisco CA 94110")
    pprint(search_foursquare("pizza", coord))
