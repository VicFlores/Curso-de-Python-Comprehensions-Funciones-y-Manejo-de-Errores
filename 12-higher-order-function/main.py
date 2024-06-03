def increment(x):
    return x + 1

def higher_order(func, x):
    return x + func(x)


result = higher_order(increment, 8)

print(result)  

# Lambda function

increment_v2 = lambda x: x + 1

higher_order_v2 = lambda func, x: x + func(x)

result_v2 = higher_order_v2(increment_v2, 8)
result_v3 = higher_order_v2(lambda x: x + 5, 8)

print(result_v2)
print(result_v3)
