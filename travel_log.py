travel_log = [

    {
    "country" : "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"],
    },

    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin" , "Hamburg" "Stuttgart"],
    }
]
def string_to_list (string_separate_comma):
    list = string_separate_comma.split(", ")
    return list
    
def add_new_country(country, visits, list_of_cities):
    new_country_dictionary = {}
    new_country_dictionary["country"] = country
    new_country_dictionary["visits"] = visits
    city_list = string_to_list(list_of_cities)
    new_country_dictionary["cities"] = city_list
    travel_log.append(new_country_dictionary)

country = input("country: ")
visits = int(input("visits: "))
list_of_cities = input("Cities visited: ")
add_new_country(country, visits, list_of_cities)

print(travel_log)