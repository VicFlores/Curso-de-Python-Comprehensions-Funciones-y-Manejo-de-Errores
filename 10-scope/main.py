# Scope: Global Scope
price = 100

print(price)

def increment():
    print(price)

increment()

# Scope: Local Scope
def increment2():
    price2 = 200
    print(price2)

increment2()
