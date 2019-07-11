import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="curl")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
