"""
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:
    make_negative(1);  # return -1
    make_negative(-5); # return -5
    make_negative(0);  # return 0

Notes:
    The number can be negative already, in which case no change is required.
    Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
"""


def make_negative(number):
    if number == 0:
        return 0
    elif number > 0:
        return number - (number + number)
    else:
        return number


print(make_negative(3))
