from collections import namedtuple
import requests

Coordinate = namedtuple("Coordinate", ["lat", "lng"])

FOURSQUARE_CLIENT_ID = "432UR1ROVWNLP0G3LU2SF3QOKZQ53XL0411G5IP3CZUQFRDO"
FOURSQUARE_CLIENT_SECRET = "1ROWRVOGF11U5FIZZLNXPYT2WP0CF3RH1M3GGIUPL2XID4XW"
GOOGLE_API_KEY = "AIzaSyCEDxxkuuwvwL8zelSLNOLqFpfTQN_LTa8"

FOURSQUARE_BASE_URL = "https://api.foursquare.com/v2/venues/search"
GOOGLE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"


def get_coordinate(city_name):
    search_url = GOOGLE_BASE_URL + "?key={}".format(GOOGLE_API_KEY)
    search_url += "&address={}".format(city_name)
    print("HTTP GET:", search_url)
    response = requests.get(search_url)
    latlong = response.json()["results"][0]["geometry"]["location"]
    return Coordinate(**latlong)


def search_foursquare(query_string, coordinate):
    search_url = FOURSQUARE_BASE_URL + "?" + query_string
    search_url += "&" + "ll={},{}".format(*coordinate)
    search_url += "&" + "client_id={}".format(FOURSQUARE_CLIENT_ID)
    search_url += "&" + "client_secret={}".format(FOURSQUARE_CLIENT_SECRET)
    search_url += "&v=20170905" + "&limit=5"
    return requests.get(search_url).json()


if __name__ == "__main__":
    from pprint import pprint
    coord = get_coordinate("2905 Harrison Street San Francisco CA 94110")
    pprint(search_foursquare("pizza", coord))
