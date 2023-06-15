from geopy.geocoders import Nominatim
from geopy import distance
import requests

geolocator = Nominatim(user_agent="127.0.0.1")

c1 = "mumbai"

l1 = geolocator.geocode(c1)
print(l1)
