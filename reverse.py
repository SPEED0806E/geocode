from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoder")

#coordinate = input("Enter a coordinate (latitude, longitude) : ")
location = geolocator.reverse("19.1326186, 72.9149702")

#print(coordinate)
print(location)
print(location.address)