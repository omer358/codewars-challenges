def add_binary(a, b):
    return str(bin(a + b)).split('b')[1]


print(add_binary(2, 3))
