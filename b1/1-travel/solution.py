
visits = {}
COMMA = ","

def collect_places():
    """
    Collect city and country on the CLI from the user
    """
    global visits
    visits = {}
    while True:
        place = input('Tell me where you went: ')
        if place == "":
            return
        elif not COMMA in place:
            print("That's not a legal city, country combination")
        else:
            city, country = place.replace(" ", "").split(",")
            existing_places = visits.get(country)
            if existing_places:
                existing_num = existing_places.get(city)
                if existing_num:
                    existing_places[city] = existing_num + 1
                else:
                    existing_places[city] = 1
                continue
            visits[country] = {city: 1}

def display_places():
    """
    Display places visited based on user input
    """
    print("You visited:")
    for country, cities in sorted(visits.items()):
        print(f"{country}")
        for city, times_visited in sorted(cities.items()):
            if times_visited > 1:
                print(f"\t{city} ({times_visited})")
            else:
                print(f"\t{city}")

if __name__ == "__main__":
    collect_places()
    display_places()
