from pprint import pprint

import requests

def catalog_of_superheroes():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    all_heroes = (response.json())

    for i in all_heroes:
        if i["name"] == "Hulk":
            Hulk_intelligence = i["powerstats"]["intelligence"]
        if i["name"] == "Captain America":
            Captain_America_intelligence = i["powerstats"]["intelligence"]
        if i["name"] == "Thanos":
            Thanos_intelligence = i["powerstats"]["intelligence"]
    if Hulk_intelligence > Captain_America_intelligence and Hulk_intelligence > Thanos_intelligence:
        print("Hulk is the smartest")
    elif Captain_America_intelligence > Thanos_intelligence:
        print("Captain_America is the smartest")
    else:
        print("Thanos is the smartest")




if __name__ == "__main__":
    catalog_of_superheroes()
