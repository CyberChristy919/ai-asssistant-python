import os
import re
import time

import folium
from geopy.geocoders import Nominatim

INPUT_FILE = os.path.expanduser('~/website_hits.txt')
OUTPUT_HTML = os.path.expanduser('~/output/website_hits_map.html')


def parse_file(path):
    entries = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            match = re.match(r'^(.*?):\s*(\d+)\s*$', line)
            if not match:
                print(f'Skipping invalid line: {line}')
                continue
            location = match.group(1).strip()
            hits = int(match.group(2))
            entries.append((location, hits))
    return entries


def geocode_locations(entries):
    geolocator = Nominatim(user_agent='website_hits_mapper_quantic')
    locations = []
    for location, hits in entries:
        result = geolocator.geocode(location, timeout=10)
        if result is None:
            print(f'Could not locate: {location}')
            continue
        locations.append({
            'location': location,
            'hits': hits,
            'lat': result.latitude,
            'lon': result.longitude,
        })
        time.sleep(1)
    return locations


def build_map(locations):
    if not locations:
        raise RuntimeError('No valid locations found.')

    average_lat = sum(item['lat'] for item in locations) / len(locations)
    average_lon = sum(item['lon'] for item in locations) / len(locations)
    map_object = folium.Map(location=[average_lat, average_lon], zoom_start=2)

    for item in locations:
        folium.Marker(
            [item['lat'], item['lon']],
            popup=f"{item['location']}: {item['hits']} hits/day",
            tooltip=item['location'],
        ).add_to(map_object)

    map_object.save(OUTPUT_HTML)


def main():
    entries = parse_file(INPUT_FILE)
    locations = geocode_locations(entries)
    build_map(locations)
    print(f'Created {OUTPUT_HTML} with {len(locations)} mapped cities.')


if __name__ == '__main__':
    main()
