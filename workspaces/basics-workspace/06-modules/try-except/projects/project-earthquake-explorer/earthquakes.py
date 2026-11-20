"""Earthquake Explorer: the earthquakes of magnitude 4.5 and above in the 30 days before 3 November 2026.

Data: U.S. Geological Survey, Earthquake Hazards Program (U.S. public domain).
Each record is a dictionary with the keys "id", "time_utc", "magnitude", "magnitude_type", "place",
"latitude", "longitude", "depth_km", "status" and "url".
"""
import json
import math

CITY = ("Tokyo", 35.68, 139.69)   # name, latitude, longitude
BANDS = ["4.5 to 4.9", "5.0 to 5.9", "6.0 to 6.9", "7.0 and above"]


# Task 2 - Correct the AI code
# An assistant might answer the request "Write load_quakes(path): read the records from the JSON file.
# If the file is missing or damaged, print a clear message and return an empty list" like this.
# Run the program, then find and fix the mistake.
def load_quakes(path):
    """Return the list of earthquake records in the JSON file at path."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


# Task 1 - Complete
# Return the label of the magnitude band, one of the four strings in BANDS.
def band(magnitude):
    # TODO: an if / elif / else chain
    return BANDS[0]


# Task 3 - Extend (optional)
# Return the distance in kilometres between two points on the Earth, given in degrees, with the
# haversine formula. The Earth's mean radius is 6,371 km.
def distance_km(lat1, lon1, lat2, lon2):
    # TODO
    return None


def report(quakes):
    strongest = max(quakes, key=lambda quake: quake["magnitude"])
    latest = max(quakes, key=lambda quake: quake["time_utc"])
    print(f"{len(quakes)} earthquakes of magnitude 4.5 and above")
    print(f"Strongest: M{strongest['magnitude']}, {strongest['place']}, {strongest['time_utc'][:10]}")
    print(f"Most recent: M{latest['magnitude']}, {latest['place']}, {latest['time_utc'][:16].replace('T', ' ')} UTC")
    counts = {label: 0 for label in BANDS}
    for quake in quakes:
        counts[band(quake["magnitude"])] += 1
    print("By magnitude:")
    for label in BANDS:
        print(f"  {label:<14} {counts[label]:>4}")
    name, lat, lon = CITY
    if distance_km(0, 0, 0, 0) is not None:
        nearest = sorted(quakes, key=lambda q: distance_km(lat, lon, q["latitude"], q["longitude"]))[:3]
        print(f"Nearest to {name}:")
        for quake in nearest:
            km = distance_km(lat, lon, quake["latitude"], quake["longitude"])
            print(f"  {km:6.0f} km  M{quake['magnitude']}, {quake['place']}")


if __name__ == "__main__":
    for path in ["earthquakes-m4.5-30-days.json", "earthquakes-truncated-copy.json", "earthquakes-missing.json"]:
        print(f"== {path}")
        quakes = load_quakes(path)
        if quakes:
            report(quakes)
        print()
