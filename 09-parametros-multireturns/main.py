def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'Vicsito'

result, width, text = find_volume(2, 3, 4)

print(result)

print(width)

print(text)

print(result)

result = find_volume()

print(result)

result = find_volume(width=4)

