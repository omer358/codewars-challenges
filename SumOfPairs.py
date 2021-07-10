def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
        print(seen)


print(sum_pairs([5, 9, 13, -3], 10))
