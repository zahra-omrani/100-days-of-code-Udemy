travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Little","Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Humburg", "Stuttgart"]
    }
]

def add_new_country(country,visits,cities):
    new_country = {
        "country":country,
        "visits":visits,
        "cities": cities
    }
    travel_log.append(new_country)

add_new_country("Russia",2,["Mascow","Saint Petersbuk"])
print(travel_log)