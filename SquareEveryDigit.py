def square_digits(num):
    num_list = [int(x) for x in str(num)]
    print(list)
    for i in range(len(num_list)):
        num_list[i] **= 2
    return int(''.join([str(n) for n in num_list]))


print(square_digits(123))
