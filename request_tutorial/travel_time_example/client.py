from typing import List, Dict, Tuple

import requests

PLACES_API = "https://places.googleapis.com/v1/places:searchText"
ROUTES_API = "https://maps.googleapis.com/maps/api/distancematrix/json"
API_KEY = ""


class Backtrack:

    def __init__(self, resorts, travel_time_map):
        self.resorts = resorts
        self.travel_time_map = travel_time_map

    def find_minimum_travel_time(self, start):
        self.visited = set()
        self.paths_map = {}
        self.path = []
        self.start = start
        self.visited.add(self.start)
        self.path.append(self.start)
        self._backtrack(self.start, 0)
        self.visited.remove(self.start)
        self.path.remove(self.start)

        min_travel_time, min_travel_path = float('inf'), None
        for path, travel_time in self.paths_map.items():
            if travel_time < min_travel_time:
                min_travel_time = travel_time
                min_travel_path = path
        sorted_d = sorted(self.paths_map, key=lambda x:self.paths_map[x])
        print("Sorted Dictionary:", sorted_d)
        return min_travel_path, min_travel_time

    def _backtrack(self, start, travel_time):
        # Base Case
        if len(self.path) == len(self.resorts):
            travel_time += self.travel_time_map[(self.path[-1], self.start)]
            self.path.append(self.start)
            self.paths_map[tuple(self.path)] = travel_time
            self.path.pop()
            return

        for resort in self.resorts:
            if resort not in self.visited:
                self.visited.add(resort)
                self.path.append(resort)
                travel_time += self.travel_time_map[(start, resort)]
                self._backtrack(resort, travel_time)
                travel_time -= self.travel_time_map[(start, resort)]
                self.visited.remove(resort)
                self.path.pop()
        return


def fetch_travel_time(p1, p1_id, p2, p2_id):
    prefix = "place_id:"
    print(f"Fetching Travel Time from {p1} to {p2}")
    param = {
        "destinations": prefix + p1_id,
        "origins": prefix + p2_id,
        "key": API_KEY
    }
    response = requests.get(ROUTES_API, params=param)
    json_response = response.json()
    return json_response['rows'][0]['elements'][0]['distance']['value']


def calculate_travel_times(place_id_map: Dict[str, str]) -> Dict[Tuple[str, str], int]:
    travel_time_map = {}
    place_id_map_list = list(place_id_map.items())
    n = len(place_id_map_list)
    for i in range(n - 1):
        p1, p1_id = place_id_map_list[i]
        for j in range(i + 1, n):
            p2, p2_id = place_id_map_list[j]
            travel_time = fetch_travel_time(p1, p1_id, p2, p2_id)
            travel_time_map[(p1, p2)] = travel_time
            travel_time_map[(p2, p1)] = travel_time
    return travel_time_map


def get_place_ids(places_names: List[str]) -> Dict[str, str]:
    place_id_map = {}
    for place_name in places_names:
        print(f"Fetching place_id for {place_name}")
        try:
            data = {"textQuery": place_name}
            headers = {"X-Goog-Api-Key": API_KEY,
                       'X-Goog-FieldMask': 'places.displayName,places.id,places.formattedAddress,places.priceLevel'}
            response = requests.post(url=PLACES_API, headers=headers, json=data)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed to query place_id: {e}")
            return {}
        json_response = response.json()
        place_id_map[place_name] = json_response['places'][0]['id']
    return place_id_map


if __name__ == "__main__":
    starting_point = "685 Mariposa Ave"
    resorts = ["350 Showers Dr, Mountain View, CA 94040", "211 Hope St, Mountain View, CA 94041",
               "615 Cuesta Dr, Mountain View, CA 94040", "988 N San Antonio Rd, Los Altos, CA 94022"]
    places = [starting_point] + resorts
    place_id_map = get_place_ids(places)

    # Places Id Map
    print(place_id_map)

    # Travel Time Map
    travel_time_map = calculate_travel_times(place_id_map)
    print(travel_time_map)

    # Find Minimum Travel Time
    backtrack = Backtrack(places, travel_time_map)
    min_travel_path, min_travel_time = backtrack.find_minimum_travel_time(start=starting_point)
    print(min_travel_path, min_travel_time)
