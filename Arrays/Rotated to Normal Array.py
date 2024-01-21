def rotated_normal_arr(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return arr[i:] + arr[:i]
    return arr


arr = [4, 5, 6, 7, 1, 2, 3]
result = rotated_normal_arr(arr)
print(result)
