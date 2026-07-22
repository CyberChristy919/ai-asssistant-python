import re
import time
from pathlib import Path

import folium
from geopy.geocoders import Nominatim

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "website_hits.txt"
OUTPUT_HTML = BASE_DIR / "website_hits_map.html"


def parse_file(path):
    entries = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            match = re.match(r"^(.*?):\s*(\d+)\s*$", line)
            if not match:
                print(f"Skipping invalid line: {line}")
                continue

            location = match.group(1).strip()
            hits = int(match.group(2))
            entries.append((location, hits))

    return entries


def geocode_locations(entries):
    geolocator = Nominatim(user_agent="website_hits_mapper")
    locations = []

    for location, hits in entries:
        try:
            result = geolocator.geocode(location, timeout=10)
        except Exception as error:
            print(f"Error looking up {location}: {error}")
            continue

        if result is None:
            print(f"Could not locate: {location}")
            continue

        locations.append(
            {
                "location": location,
                "hits": hits,
                "lat": result.latitude,
                "lon": result.longitude,
            }
        )

        time.sleep(1)

    return locations


def build_map(locations):
    
