# Sets
# Se pueden modificar
# No tienen un orden
# No pueden tener elementos duplicados

set_countries = {'col', 'mex', 'sv'}

print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5}

print(set_numbers)
print(type(set_numbers))

set_mixed = {1, 'col', 3.14}

print(set_mixed)
print(type(set_mixed))

set_from_string = set('colombia')

print(set_from_string)

set_from_tuple = set(('abc', 'cdv', 'dsq'))

print(set_from_tuple)

numbers = [1, 2, 3, 4, 2, 4, 7,8,9]

set_from_list = set(numbers)

print(set_from_list)

unique_numbers = list(set_from_list)