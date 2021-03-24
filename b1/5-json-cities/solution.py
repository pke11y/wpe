from urllib.request import urlopen
import csv
import io
import json
import requests

gist_url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"

header = ['city', 'rank', 'population', 'state']

def cities_to_csv(url: str, fname: str):
    cities_json = get_log_file(url)
    city_list = json.loads(cities_json)
    # print(city_dict)
    rows = [(city.get('city'), city.get('population'), city.get('rank'), city.get('state')) for city in city_list]
    print(rows)

def get_log_file(fname: str):
    """
    Retrieve the JSON file.
    """
    if fname.startswith(("https:", "http:", "ftp:")):
        return urlopen(fname).read()
    with open(fname) as f:
        return f.read()

if __name__ == "__main__":
    cities_to_csv(gist_url, "cities.csv")