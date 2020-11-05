import random
cities = []

cities.append(input("Where were you born? "))
cities.append(input("What is your favorite city in the world? "))
cities.append(input("Which city could you see yourself living in? "))

pets = []

pets.append(input("What kind of pet do you own? "))
pets.append(input("What is your favorite exotic animal? "))
pets.append(input("Name a pet that you wish were domesticated? "))

print("Your band name is " + cities[random.randrange(0,2)] +  " " + pets[random.randrange(0,2)])