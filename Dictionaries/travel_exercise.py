''' Write a program that adds to a travel_log. You can see that travel_log which is a List that contains 2 Dictionaries.'''

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



