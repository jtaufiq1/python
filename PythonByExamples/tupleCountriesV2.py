#!/usr/bin/python3

# Container: Tuple
# Contains: Names of 5 countries
# Display names countries
# Get name of country
# Display index of the country in the tuple

COUNTRIES = ("Ghana","Kuwait","Jordan","Saudi Arabia","North Korea")

print(COUNTRIES)
country = input("Enter country name: ")
country = country.title()

if country in COUNTRIES:
    print(f"{country} is at position {COUNTRIES.index(country)}")
else:
    print(f"{country} not in list")

# Version 2
# Get index of a country
# Display the country at that index

index = int(input("Enter a number: "))

if index < 0 or index >= len(COUNTRIES):
    print(f"{index} not in list")
else:
    print(f"{COUNTRIES[index]}")
