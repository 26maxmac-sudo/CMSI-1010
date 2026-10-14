import random
from havershine import haversine
from geography import countries


def random_country_name():
    # Select a random country name from the key in the countries dictionary we imported.
    # We have to convert the keys to a list, because random.choice() only works on lists,
    # and the keys of a dictionary are (surprisingly!) not a list in Python.
    return random.choice(list(countries.keys()))


def random_hint(country):
    hint_type = random.choice(["capital", "region", "landmark", "distance"])
    if hint_type == "capital":
        hint = "whose capital is " + country["capital"]
    elif hint_type == "region":
        hint = "in " + country["region"]
    elif hint_type == "landmark":
        hint = "where you can find " + random.choice(country["landmarks"])
    elif hint_type == "distance":
        los_angeles = (34.0522, -118.2437)
        from_LA = haversine(los_angeles, country["coordinates"], unit="km")
        hint = "approximately " + str(from_LA) + " km from Los Angeles"

    return "Carmen is in a country " + hint


current_country_name = random_country_name()
while True:
    country = countries[current_country_name]
    print("Guess where Carmen is, or say 'hint' or 'exit'.")
    guess = input("Where are you going to look? ").strip().lower()
    if guess == current_country_name:
        print("She was here, but you missed her by one hour!")
        current_country_name = random_country_name()
    elif guess == "hint":
        print(random_hint(country))
    elif guess == "exit":
        print("Thank you for playing!")
        break
    else:
        print("Oh no, she’s not here!")