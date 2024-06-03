# Funciones de set:

# add(): Añade un elemento.

# update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

# discard(): Elimina un elemento y si ya existe no lanza ningún error.

# remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

# pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

# clear(): Elimina todo el contenido del conjunto.

set_countries = {'col', 'mex', 'sv'}

size = len(set_countries)

print(size)

exists = 'col' in set_countries

print(exists)

set_countries.add('arg')

print(set_countries)

set_countries.update({'per', 'chi'})

print(set_countries)

set_countries.discard('mex')

print(set_countries)

set_countries.remove('sv')

print(set_countries)

set_countries.clear()

print(set_countries)