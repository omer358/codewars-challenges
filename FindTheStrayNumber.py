"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
    [1, 1, 2] ==> 2
    [17, 17, 3, 17, 17, 17, 17] ==> 3
"""


def stray(arr):
    for i in arr:
        if arr.count(i) % 2 != 0:
            return i


print(stray([1, 3, 2, 3, 2, 4, 4]))
