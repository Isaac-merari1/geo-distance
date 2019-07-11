
from geopy import distance
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="distance.py")

def create_location(city):
  location = geolocator.geocode(city)
  return (location.latitude, location.longitude)

city1 = create_location("Accra")
city2 = create_location("Kumasi, Ghana")


print("The distance between" +  city1" and" city2" is" + str( distance.distance(city1, city2).kilometers))


