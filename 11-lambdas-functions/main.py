# ¿Que es lambda? Son conocidas como Funciones Anónimas o lambdas, en donde no tienen un identificador o no tienen un nombre, se puede definir su estructura de la siguiente manera: lambda argumentos: expresión, las funciones lambda pueden tener los argumentos que se requieran pero solo una linea de código o una expresión.

# Sintaxis
# lambda arguments : expression


def increment(x):
    return x + 1

print(increment(5))

# Lambda Function
lambda x: x + 1

# Lambda Function with a variable
increment = lambda x: x + 1

print(increment(4))

full_name = lambda name, lastname: f'{name} {lastname}'

print(full_name('Vic', 'Flores'))