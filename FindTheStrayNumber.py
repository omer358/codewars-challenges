def stray(arr):
    for i in arr:
        if arr.count(i) % 2 != 0:
            return i


print(stray([1, 3, 2, 3, 2, 4, 4]))
