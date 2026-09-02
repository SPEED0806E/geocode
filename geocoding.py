from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import sqlite3
# create a geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# connect to the database
conn = sqlite3.connect("location.db")
cursor = conn.cursor()

# create a table to store the places
cursor.execute("""
CREATE TABLE IF NOT EXISTS places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
)
""")

# search for a place
place = input("Enter a place name : ").capitalize()
location = geolocator.geocode(place)

# print the result
if location:
    print(place)
    print(location)
    print(location.latitude)
    print(location.longitude)
    # print(location.raw["address"])

    # save the place to the database
    cursor.execute("""
    INSERT INTO places (name, latitude, longitude)
    VALUES (?, ?, ?)
    """, (place, location.latitude, location.longitude))

    conn.commit()

    cursor.execute("SELECT * FROM places")
    rows = cursor.fetchall()
    print("previous searches :")
    for row in rows:
        print(row)

    print("Saved to database")

else:
    print("Place not found")

    conn.close()

location_a = (19.1326186, 72.9149702)
location_b = (18.9229, 72.8347)

distance = geodesic(location_a, location_b)

print(distance)
print(distance.meters)