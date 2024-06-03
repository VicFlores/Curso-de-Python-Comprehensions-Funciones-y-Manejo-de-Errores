import random
dict = {}

for i in range(1, 11):
    dict[i] = i * 2

print(dict)

# Dictionary comprehension
dict_v2 = {i: i * 2 for i in range(1, 11)}
print(dict_v2)


countries = ['Brazil', 'Argentina', 'Uruguay', 'Chile']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
            # Brazil    :  10
            # Argentina :  20
            # Uruguay   :  30
            # Chile     :  40

print(population)

# Dictionary comprehension
population_v2 = {country: random.randint(1, 100) for country in countries }
print(population_v2)


names = ['John', 'Jane', 'Alice', 'Bob']
age = [20, 30, 40, 50]

# Dictionary comprehension
new_dict = {name:age for (name, age) in zip(names, age)}
print(new_dict)
