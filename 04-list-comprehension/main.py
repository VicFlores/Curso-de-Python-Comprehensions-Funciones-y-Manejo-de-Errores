numbers = []


for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

# List comprehension
numbers_v2 = [(element * 2) for element in range(1,11)]
print(numbers_v2)

# List comprehension with condition
even_numbers = [(element * 2) for element in range(1,20) if element % 2 == 0]
print(even_numbers)

animals = ['cat', 'dog', 'elephant', 'bird']

# List comprehension with string
animals_v2 = [animal.upper() for animal in animals]
print(animals_v2)
