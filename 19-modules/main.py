import re
import sys
import time
import collections


print(sys.path)

text = "Mi numero de telefono es 123-456-7890, el codigo de area es 123, mi numero de la suerte es 7"

result = re.findall('[0-9]+', text)

print(result)

timestamp = time.time()
local = time.localtime(timestamp)
result = time.asctime(local)

print(timestamp)
print(local)
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

counter = collections.Counter(numbers)

print(counter)
