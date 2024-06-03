import random

countries = ['Brazil', 'Argentina', 'Uruguay', 'Chile']

population = {country: random.randint(1, 100) for country in countries}

print(population)

# Dictionary comprehension with condition
population_v2 = {country: population for (country, population) in population.items() if population > 20}
print(population_v2)


text = 'Hola, Vic'

unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)