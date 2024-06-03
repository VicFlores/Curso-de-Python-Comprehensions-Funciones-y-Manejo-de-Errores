items = [
    {"name": "item1", "price": 10},
    {"name": "item2", "price": 20},
    {"name": "item3", "price": 30},
    {"name": "item4", "price": 40},
    {"name": "item5", "price": 50}
]

prices = list(map(lambda item: item['price'], items ))
# creamos lista / map / item {"name": "item1", "price": 10} / item['price'] = 10 / items array

print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.16
    return item

new_items = list(map(add_taxes, items))

print(items)
print(new_items)