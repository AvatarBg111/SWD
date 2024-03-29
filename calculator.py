def sum(x, y): 
    return x + y

def diff(x, y):
    return x - y

def multiplication(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

print(sum(1, 2))
print(diff(3, 2))
print("5 * 6 = " + str(multiplication(5, 6)))
print("5 / 6 = " + str(divide(5, 6)))