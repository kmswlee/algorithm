def sumOddLengthSubarrays(arr):
    res, n = 0, len(arr)
    for i, a in enumerate(arr):
        res += int(((i + 1) * (n - i) + 1) / 2) * a
    return res

arr = [1,4,2,5,3]

print(sumOddLengthSubarrays(arr))
    