sum = 0

for x in range (1, 11):
    sum += x

print(sum) 

def add_numbers(a, b):
    sum = 0

    for x in range (a, b + 1):
        sum += x
    return sum

print(add_numbers(1, 10))
print(add_numbers(1, 20))

