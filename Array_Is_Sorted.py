def is_sorted(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# Example array
arr = [1, 2, 3, 4, 5]

if is_sorted(arr):
    print("Array is sorted")
else:
    print("Array is not sorted")