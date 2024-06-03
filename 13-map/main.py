numbers = [1, 2, 3, 4, 5]
numbers_v2 = []
numbers_v3 = []

for i in numbers:
    numbers_v2.append(i + 1)

print(numbers)
print(numbers_v2)

# Using map function

numbers_v3 = map(lambda x: x * 2, numbers)

print(list(numbers_v3))

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

result = map(lambda x,y: x + y, numbers_1, numbers_2)

print(numbers_1)
print(numbers_2)
print(list(result))

