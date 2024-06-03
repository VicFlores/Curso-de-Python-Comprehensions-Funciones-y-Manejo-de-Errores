file = open(r'24-read-files\text.txt')

# leer el contenido del archivo
# print(file.read())

# leer linea por linea
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for line in file:
    print(line)

# cerrar el archivo
file.close()


# with open
with open(r'24-read-files\text.txt') as file:
    for line in file:
        print(line)


with open(r'24-read-files\text.txt') as file:
    lines = file.readlines()
    print(lines)
