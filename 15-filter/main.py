# FILTER
# La función filter(), devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(new_numbers)
