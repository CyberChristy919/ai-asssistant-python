import re
from pathlib import Path

import folium
from geopy.geocoders import Nominatim

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "website_hits.txt"
OUTPUT_FILE = BASE_DIR / "website_hits_map.html"

geolocator = Nominatim(user_agent="website_hits_map")

m = folium.Map(location=[20, 0], zoom_start=2)

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        match = re.match(r"^(.*?):\s*(\d+)$", line)
        if not match:
            continue

        city = match.group(1)
        hits = match.group(2)

        location = geolocator.geocode(city)
        if location:
            folium.Marker(
                [location.latitude, location.longitude],
                popup=f"{city}: {hits}"
            ).add_to(m)

m.save(OUTPUT_FILE)
print("Map created:", OUTPUT_FILE)
