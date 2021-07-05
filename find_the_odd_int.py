"""
6KYU
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it([1, 1, 2, 3, 2, 5, 4, 3, 5]))
