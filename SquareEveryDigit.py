"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    num_list = [int(x) for x in str(num)]
    print(list)
    for i in range(len(num_list)):
        num_list[i] **= 2
    return int(''.join([str(n) for n in num_list]))


print(square_digits(123))
