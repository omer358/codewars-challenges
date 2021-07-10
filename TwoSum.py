"""
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.
The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater,
and all of the items will be numbers; target will always be the sum of two different items from that array).

Example:
    twoSum [1, 2, 3] 4 === (0, 2)
"""


def two_sum(numbers, target):
    num_index = 0
    for number in numbers:
        index = 1
        while index < len(numbers):
            if number + numbers[index] == target:
                return [num_index, index]
            index += 1
        num_index += 1

    return [0, len(numbers)-1]


print(two_sum([2, 2, 3], 4))
